#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
import re

import func

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

func.faxlog("notify> Executing: {0} {1} {2} {3} ({4})".format(qfile, why, jobtime, nextTry), True)

faxdone = False
fatal = False
alert = False

if why == "done":
    faxdone = True
elif why == "blocked" or why == "requeued":
    alert = True
else:
    fatal = True

file_data = file(qfile)
faxfiles = []
file_cnt = 0

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

