import re
import datetime
from pymongo import MongoClient


def strip_sipinfo(callid):
    comp = re.compile(r"^(.*)@(.*)$")
    matches = comp.match(callid)
    print("Strip sipinfo : ", matches)
    if matches is not None:
        callid = matches
    return callid

def faxlog(logText, echo):
    echo = True if echo else False

    client = MongoClient('localhost', 27017)
    db = client['zyapp']
    syslog = db.syslogs
    log = {"logtext": logText,
           "logdate": datetime.datetime.utcnow()}
    syslog.insert_one(log)

    if echo:
        print(logText)
