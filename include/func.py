import re
import datetime
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
