#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
from datetime import datetime
from os import path


import constant
import func
from lang import LANG
from models import AFAddressBook, AFUserAccount, ArchiveOut

argc = len(sys.argv)

if argc < 3:
    sys.exit("Usage: {0} qfile why jobtime [nextTry]".format(sys.argv[0]))


debug = False
quiet = True

qfile = sys.argv[1]
why = sys.argv[2]
jobtime = sys.argv[3] if argc >= 4 else None
nextTry = sys.argv[4] if argc >= 5 else None

if not path.exists(qfile):
    sys.exit("{0} doesn't exist".format(qfile))

func.faxlog("notify> Executing: {0} {1} {2} {3} ({4})".format(qfile, why, jobtime, nextTry, argc), True)

faxdone = False
fatal = False
alert = False

if why == "done":
    faxdone = True
elif why in ["blocked", "requeued"]:
    alert = True
else:
    fatal = True

file_data = open(qfile)
faxfiles = []
file_cnt = 0

totpages = None
status = None
external = None
jobid = None
mailaddr = None
groupid = None
to_location = None
to_voice = None
to_person = None
to_company = None
regarding = None
owner = None

for line in file_data:
    line = line.strip()
    line_info = line.split(":")

    if line_info[0] == "totpages":
        totpages = line_info[1]
        print("{0}: {1}".format(line_info[0], totpages))
    elif line_info[0] == "status":
        status = line_info[1]
        print("{0}: {1}".format(line_info[0], status))
    elif line_info[0] == "external":
        external = func.clean_faxnum(line_info[1])
        print("{0}: {1}".format(line_info[0], external))
    elif line_info[0] == "jobid":
        jobid = line_info[1]
        print("{0}: {1}".format(line_info[0], jobid))
    elif line_info[0] == "mailaddr":
        mailaddr = line_info[1]
        print("{0}: {1}".format(line_info[0], mailaddr))
    elif line_info[0] == "groupid":
        groupid = line_info[1]
        print("{0}: {1}".format(line_info[0], groupid))
    elif line_info[0] == "location":
        to_location = line_info[1] if func.isset(line_info[1]) else None
        print("{0}: {1}".format(line_info[0], to_location))
    elif line_info[0] == "voice":
        to_voice = line_info[1] if func.isset(line_info[1]) else None
        print("{0}: {1}".format(line_info[0], to_voice))
    elif line_info[0] == "receiver":
        to_person = line_info[1] if func.isset(line_info[1]) else None
        print("{0}: {1}".format(line_info[0], to_person))
    elif line_info[0] == "company":
        to_company = line_info[1] if func.isset(line_info[1]) else None
        print("{0}: {1}".format(line_info[0], to_company))
    elif line_info[0] == "regarding":
        regarding = line_info[1] if func.isset(line_info[1]) else None
        print("{0}: {1}".format(line_info[0], regarding))
    elif line_info[0] == "owner":
        owner = line_info[1].lower()
        print("{0}: {1}".format(line_info[0], owner))
    elif re.match(r"postscript", line_info[0]) or re.match(r"pdf", line_info[0]) or re.match(r"tiff", line_info[0]):
        print("Found file: {0}".format(line_info[3]))
        if not re.match(r"\;", line_info[3]):
            faxfiles.append(line_info[3])
            file_cnt += 1

if not to_company:
    to_company = external

addressbook = AFAddressBook()
mult = []

if addressbook.loadbyfaxnum(external, mult):
    if mult[0]:
        cid = 0
        func.faxlog("notify> Found fax number with multiple companies", True)
    else:
        cid = addressbook.get_companyid()
        addressbook.inc_faxto()
else:
    if addressbook.create(to_company):
        if addressbook.create_faxnumid(external):
            addressbook.save_settings({'description': None, 'faxcatid': None, 'to_person': to_person, 'to_location': to_location, 'to_voicenumber': to_voice})

            cid = addressbook.get_companyid()
            addressbook.inc_faxto()
            func.faxlog("notify> Created company '{0}' with cid '{1}'".format(external, cid), True)
        else:
            cid = 0
            func.faxlog("notify> FAILED to create faxnumid for '{0}' - {1}".format(external, addressbook.get_error()), True)
    else:
        cid = 0
        func.faxlog("notify> FAILED to create company '{0}' - {1}".format(external, addressbook.get_error()), True)

from_email = func.get_admin_email()
to_email = ""

user = AFUserAccount()
user_id = 0

if owner == constant.FAXMAILUSER or owner == constant.WWWUSER:
    if user.loadbyemail(mailaddr):
        owner = user.username
        to_email = user.email
        user_id = user.get_uid()
    else:
        to_email = mailaddr
        func.faxlog("notify> Failed to load account for email '{0}' - {1}".format(mailaddr, user.get_error()), True)
else:
    if not user.load_username(owner):
        to_email = mailaddr
        func.faxlog("notify> Failed to load account name '{0}' - {1}".format(owner, user.get_error()), True)
    else:
        to_email = user.email
        user_id = user.get_uid()

company = addressbook.get_company()
if company:
    pass
else:
    company = external

# send confirmation email the fax to sender
subject = "fax: {0} {1}".format(company, datetime.now().strftime(constant.EMAIL_DATE_FORMAT))
text = "{0}: {1}".format(LANG['TO'], company)

desc = addressbook.get_description()
if desc:
    text = text + ' ({0})'.format(desc)

if regarding:
    text = text + '\nRe: {0}\n'.format(regarding)

# if fatal, notify sender
if fatal:
    subject = "{0} {1}".format(LANG['FAX_WHY'][why], subject)
    text = "{0}: {1} {2}\n\n{3}".format(LANG['FAX_FAILED'], LANG['FAX_WHY'][why], status, text)

    faxpath = path.join(constant.TMPDIR, '{0}{1}-{2}-{3}'.format(datetime.now().strftime('%Y-%m-%d-'), external, datetime.now().strftime('%H%i%s'), jobid))
    os.makedirs(faxpath)

    if func.convert2pdf(faxpath, faxfiles):
        print("Emailing pdf file to %s" % to_email)
        pdf_file = path.join(faxpath, constant.PDFNAME)
        func.send_mail(to_email, from_email, subject, text, pdf_file, external+".pdf")
        os.unlink(pdf_file)
        os.rmdir(faxpath)
    else:
        func.faxlog("notify> FAILED to create PDF for failed fax", True)
        func.send_mail(to_email, from_email, subject, text+"\nFAILED to create PDF for failed fax")
    sys.exit()

if alert:
    subject = "Fax {0} {1} {2} {3}".format(groupid, LANG['TO'], external, LANG['FAX_WHY'][why])
    text = "{0} {1}\n\n{2}".format(LANG['FAX_WHY'][why], status, text)

    if nextTry:
        text += "\nFAX -> {0}".format(nextTry)
    func.send_mail(to_email, from_email, subject, text)
    sys.exit()

if not faxdone:
    sys.exit()

now = datetime.now()
faxpath = path.join(constant.ARCHIVE_SENT, now.year, now.month, now.day, external, now.strftime("%H%i%s"), jobid)
os.makedirs(faxpath)

if func.convert2pdf(faxpath, faxfiles):
    pdf_file = path.join(faxpath, constant.PDFNAME)
    thumbnail = path.join(faxpath, constant.THUMBNAIL)

    func.pdf_preview(faxpath)

    outbox = ArchiveOut()
    if outbox.create(faxpath, user_id, cid, external, totpages):
        text += "\nFax ID: {0}\n{1}: {2}\n".format(outbox.get_fid(), LANG['PN_PAGES'], totpages)
        if regarding:
            regarding = func.decode_entity(regarding)
            outbox.set_note(regarding, None, user_id)
    else:
        func.faxlog("notify> FAILED to add Sent fax '{0}' to ArchiveOut".format(faxpath), True)

    if constant.NOTIFY_ON_SUCCESS:
        func.send_mail(to_email, from_email, subject, "Fax: OK\n\n"+text, pdf_file if constant.NOTIFY_INCLUDE_PDF else None,
                       external+'.pdf' if constant.NOTIFY_INCLUDE_PDF else None, None if constant.NOTIFY_INCLUDE_PDF else thumbnail)
        func.faxlog("notify> Notification email sent to "+to_email, True)
    else:
        func.faxlog("notify> Skipping notification email to {0} as per config setting NOTIFY_ON_SUCCESS".format(to_email), True)
else:
    func.faxlog("notify> FAILED to create PDF for Archive", True)
    func.send_mail(to_email, from_email, subject, "Fax: OK\nFailed to create PDF for Archive\n\n"+text)

print("Done")
sys.exit()
