#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import func
from models import DynamicConfig

if len(sys.argv) == 1:
    print("%s device CallID1 CallIDn ..." % sys.argv[0])
    sys.exit(1)

device = sys.argv[1]
callid1 = None

if len(sys.argv) > 2:
    if sys.argv[2] is None:
        callid1 = "EMPTY CALLID"
    else:
        callid1 = func.strip_sipinfo(sys.argv[2])

    print("CallID1 : %s" % callid1)

    func.faxlog("dynconf> checking CallID1 {0} on device {1}".format(callid1, device), True)

    dc = DynamicConfig()

    if dc.lookup(device, callid1):
        func.faxlog("dynconf> rejecting {0} on device {1}".format(callid1, device), True)
        print("RejectCall: true")
