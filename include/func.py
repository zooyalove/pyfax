import os, shutil, subprocess
import time, math, hashlib
import re, datetime, html, textwrap

from os import path
from pymongo import MongoClient

import constant
from models import Mailer


def microtime(get_as_float=False):
    if get_as_float:
        return time.time()
    else:
        return '%f %d' % math.modf(time.time())


def genpasswd(l=constant.MIN_PASSWD_SIZE):
    m = hashlib.md5(microtime()).hexdigest()
    return m[:l]


def tmpfilename(suffix):
    return path.join(constant.TMPDIR, 'avantfax-'+genpasswd()+'.'+suffix)


def file_get_contents(filename):
    """
    파일을 읽어들여 문자열 형태로 반환. 만약에 읽기 실패할 경우 False값을 반환한다.
    :param filename: str
    :return: string or False 
    """
    try:
        ret = open(filename).read()
    except:
        ret = False

    return ret


def isset(var):
    try:
        var
    except NameError:
        var = None
    
    if var is None:
        return False
    return True


def strip_sipinfo(callid):
    comp = re.compile(r"^(.*)@(.*)$")
    matches = comp.match(callid)
    print("Strip sipinfo : ", matches)
    if matches is not None:
        callid = matches
    return callid


def faxlog(logText, echo=False):
    echo = True if echo else False

    client = MongoClient('localhost', 27017)
    db = client['zyapp']
    syslog = db['syslogs']
    log = {"logtext": logText,
           "logdate": datetime.datetime.utcnow()}
    syslog.insert_one(log)

    if echo:
        print(logText)


def sendmaillog(logtext):
    log = logtext.replace('<', '&lt;')
    log = log.replace('>', '&gt;')
    log = log.replace('"', '&quot;')
    faxlog("send_mail> "+log)


def clean_faxnum(fnum):
    res = re.sub(r"[^\+\w]", "", fnum)
    return res


def get_admin_email():
    return constant.ADMIN_EMAIL


def chunk_split(body, chunklen=76, end='\r\n'):
    return end.join(textwrap.wrap(body, chunklen))


def convert2pdf(faxpath, convertfiles):
    # GSCMD, TIFFPS, GSR
    pdffile = path.join(faxpath, constant.PDFNAME)
    # tiffile = path.join(faxpath, constant.TIFFNAME)

    convert_tiff = []
    del_tif = []

    convert_ps = ""
    coverpage = None
    tmpcover = None
    list_pdf = ""
    tmpps = None
    tmptif = None

    print("convert2pdf> starting")

    for i in range(len(convertfiles)):
        if re.search(r"\.tif", convertfiles[i]):
            convert_tiff.append(convertfiles[i])
        elif re.search(r"\.ps", convertfiles[i]):
            convert_ps += convertfiles[i] + " "
        elif re.search(r"cover", convertfiles[i]):
            coverpage = convertfiles[i]
        else:
            list_pdf += convertfiles[i] + " "

    time_start = microtime(True)

    if isset(coverpage):
        print("convert2pdf> converting coverpage to pdf")
        tmpcover = tmpfilename('pdf')
        cmd = constant.GSCMD % (tmpcover, coverpage)
        subprocess.call(cmd, shell=True)
        list_pdf = "{0} {1}".format(tmpcover, list_pdf)

    if isset(convert_ps):
        print("convert2pdf> converting postscript to pdf")
        tmpps = tmpfilename('pdf')
        cmd = constant.GSCMD % (tmpps, convert_ps)
        subprocess.call(cmd, shell=True)
        list_pdf += tmpps + " "

    if type(convert_tiff) is list:
        print("convert2pdf> processing tiffs")
        for tiff in convert_tiff:
            tmptif = tmpfilename('pdf')
            subprocess.call("{0} {1} | {2} -sOutputFile={3} - -c quit {4}".format(constant.TIFFPS, tiff, constant.GSR, tmptif, None), shell=True)
            list_pdf += tmptif+" "
            del_tif.append(tmptif)

    if isset(list_pdf):
        list_pdf = list_pdf.strip()
        cnt = list_pdf.split(" ")

        if len(cnt) > 1:
            print("convert2pdf> creating final pdf")
            cmd = constant.GSCMD % (pdffile, list_pdf)
            subprocess.call(cmd, shell=True)
        else:
            print("convert2pdf> copying {0} to {1}".format(list_pdf, pdffile))
            shutil.copyfile(list_pdf, pdffile)

    time_end = microtime(True)
    os.chmod(pdffile, 0o666)
    print("convert2pdf> cleaning up...")

    if isset(tmpps):
        os.unlink(tmpps)
    if isset(tmpcover):
        os.unlink(tmpcover)
    if type(del_tif) is list:
        for tiff in del_tif:
            os.unlink(tiff)

    print("done")

    ret = True

    if not path.isfile(pdffile):
        faxlog("convert2pdf> failed to create" + pdffile, True)
        ret = False
    else:
        time = round(time_end - time_start, 1)
        faxlog("convert2pdf> created {0} in {1}ms".format(pdffile, time), True)

    return ret


def split_emails(emails):
    emails = decode_entity(emails)
    to_addy = emails.split(r'[;]')
    to_addy = [ t.strip() for t in to_addy]

    return to_addy


def new_mailer(from_email, subject, text):
    mailer = Mailer()

    mailer.setFrom(decode_entity(from_email))
    mailer.setSubject(decode_entity(subject))
    mailer.set_message(text)

    return mailer


def send_mail(to_email, from_email, subject, text, file=None, altname=None, cc=None, bcc=None):
    mailer = new_mailer(from_email, subject, text)
    mailer.attach_file(file, altname)

    if cc:
        mailer.setCc(split_emails(cc))

    if bcc:
        mailer.setBcc(split_emails(bcc))

    emails = split_emails(to_email)

    if mailer.sendmail(emails):
        sendmaillog("'%s' sent to '%s' from '%s' - %s (%s)" % (subject, to_email, from_email, file, altname))
        return True

    sendmaillog("FAILED to send '%s' to '%s' from '%s' - %s (%s)" % (subject, to_email, from_email,file, altname))
    faxlog("send_mail> MAIL ERROR: %s" % mailer.get_error())
    return False


def pdf_preview(faxpath, quiet):
    faxfile = path.join(faxpath, constant.PDFNAME)

    if path.exists(faxfile):
        tmpfile = tmpfilename('tif')
        preview = path.join(faxpath, constant.THUMBNAIL)
        final_file = path.join(faxpath, constant.PREVIMG+'0'+constant.PREVIMGSFX)
        is_quiet = ">/dev/null 2>/dev/null" if quiet else None

        if subprocess.check_call("{0} -sOutputFile={1} {2} -c quit {3}".format(constant.GSN2, tmpfile, faxfile, is_quiet), shell=True) == 0:
            subprocess.call("{0} -width {1} {2} 2>/dev/null | {3} 31 | {4} 2>/dev/null > {5}".format(constant.PNMSCALE, constant.PREV_TN, tmpfile, constant.PNMDEPTH, constant.PPMTOGIF, preview), shell=True)

            if not os.stat(preview).st_size:
                faxlog("static_preview> Using pnmquant to create "+preview)
                subprocess.call("{0} -width {1} {2} 2>/dev/null | {3} 31 | {4} 256 2>/dev/null | {5} 2>/dev/null > {6}".format(constant.PNMSCALE, constant.PREV_TN, tmpfile, constant.PNMDEPTH, constant.PNMQUANT, constant.PPMTOGIF, preview), shell=True)

            subprocess.call("{0} -width {1} {2} 2>/dev/null | {3} 31 | {4} 2>/dev/null > {5}".format(constant.PNMSCALE, constant.PREV_SP, tmpfile, constant.PNMDEPTH, constant.PPMTOGIF, final_file), shell=True)

            if not os.stat(final_file).st_size:
                faxlog("static_preview> Using pnmquant to create "+final_file)
                subprocess.call("{0} -width {1} {2} 2>/dev/null | {3} 31 | {4} 256 2>/dev/null > {5} 2>/dev/null > {6}".format(constant.PNMSCALE, constant.PREV_SP, tmpfile, constant.PNMDEPTH, constant.PNMQUANT, constant.PPMTOGIF, final_file), shell=True)

        else:
            faxlog("pdf_preview> failed to generate "+preview, True)
            shutil.copyfile(constant.NOTHUMBIMG, preview)

        if path.exists(tmpfile):
            os.unlink(tmpfile)

    else:
        faxlog("pdf_preview> %s doesn't exist" % faxfile, True)


def decode_entity(description):
    return html.unescape(description)
