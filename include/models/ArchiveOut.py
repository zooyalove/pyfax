from datetime import datetime
import constant
import func
from . import FaxPDFArchive


class ArchiveOut(FaxPDFArchive):
    def __init__(self):
        super(FaxPDFArchive, self).__init__()

        self.faxpath = None
        self.userid = None
        self.pages = None
        self.companyid = None
        self.origfaxnum = None

    def create(self, faxpath, userid, cid, origfaxnum, pages):
        self.faxpath = faxpath
        self.userid = userid
        self.pages = pages
        self.companyid = cid
        self.origfaxnum = func.clean_faxnum(origfaxnum)

        self.faxpath = self.faxpath.replace(constant.INSTALLDIR, "")

        res =  self._collection.insert_one({'userid': self.userid, 'faxpath': self.faxpath, \
                                        'companyid': self.companyid, 'archstamp': datetime.utcnow(), 'inbox': False, \
                                        'origfaxnum': self.origfaxnum, 'pages': self.pages})
        if res:
            self._dbdata['fid'] = res.inserted_id
        else:
            self.set_error("No fid created")
            func.faxlog("class ArchiveOut> Fax not inserted into database for faxpath '{0}'".format(self.faxpath))
            return False

        func.faxlog("class ArchiveOut> fax '{0}' sent by userid '{1}' to companyid '{2}'".format(self.faxpath, self.userid, self.companyid))
        return True
