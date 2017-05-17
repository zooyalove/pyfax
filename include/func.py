import re, datetime, html
import time, math, hashlib
import subprocess
from os import path
from pymongo import MongoClient

import constant

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

def convert2pdf(faxpath, convertfiles):
    # GSCMD, TIFFPS, GSR
    pdffile = path.join(faxpath, constant.PDFNAME)
    tiffile = path.join(faxpath, constant.TIFFNAME)

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
            subprocess.call("{0} {1} | {2} -sOutputFile={3} - -c quit {4}".format(constant.TIFFPS, tiff, constant.GSR, tmptif, is_quiet))

def send_mail(to_email, from_email, subject, text, file=None, altname=None, embedd=None, cc=None, bcc=None):
    pass

def pdf_preview(faxpath):
    pass

def decode_entity(description):
    return html.unescape(description)
