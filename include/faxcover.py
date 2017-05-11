#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import getopt
import constant
import func

options = getopt.getopt("t:c:p:l:m:z:r:v:x:C:D:L:N:V:X:s:f:n:M:")

if not options['f'] or not options['n']:
    exit("""
    Usage: faxcover [-t to] [-c comments] [-p #pages] [-l to-location] [-m maxcomments] [-z maxlencomments]
			        [-r regarding] [-v to-voice-number] [-x to-company] [-C template-file] [-D date-format] [-L from-location]
			        [-M from-mail-address] [-N from-fax-number] [-V from-voice-number] [-X from-company] [-s pagesize] -f from -n fax-number
    """)

using_html_cp = False
coverpage_file = constant.INSTALLDIR + '/images/' + constant.COVERPAGE_FILE

from_name = options['f']
from_email = options['M'] if options['M'] else None

func.faxlog("faxcover> from: '{0}' email: '{1}'".format(from_name, from_email))
