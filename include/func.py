import re, datetime, html
from os import path
from pymongo import MongoClient

import constant

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
    syslog = db.syslogs
    log = {"logtext": logText,
           "logdate": datetime.datetime.utcnow()}
    syslog.insert_one(log)

    if echo:
        print(logText)

def clean_faxnum(fnum):
    res = re.sub(r"[^\+\w]", "", fnum)
    return res

def get_admin_email():
    return constant.ADMIN_EMAIL

def convert2pdf(faxpath, faxfiles):
    # GSCMD, TIFFPS, GSR
    pdffile = path.join(faxpath, constant.PDFNAME)
    tiffile = path.join(faxpath, constant.TIFFNAME)

    convert_tiff = []
    del_tif = []

    convert_ps = None
    coverpage = None
    tmpcover = None
    list_pdf = None
    tmpps = None
    tmptif = None

    print("convert2pdf> starting")

def send_mail(to_email, from_email, subject, text, file=None, altname=None, embedd=None, cc=None, bcc=None):
    pass

def pdf_preview(faxpath):
    pass

def decode_entity(description):
    return html.unescape(description)
