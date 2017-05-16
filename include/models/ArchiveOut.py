import constant
import func
from . import FaxPDFArchive


class ArchiveOut(FaxPDFArchive):
    def __init__(self):
        super(FaxPDFArchive, self).__init__()


    def create(self, faxpath, userid, cid, origfaxnum, pages):
        self.faxpath = faxpath
        self.userid = userid
        self.pages = pages
        self.companyid = cid
        self.origfaxnum = func.clean_faxnum(origfaxnum)

        self.faxpath = self.faxpath.replace(constant.INSTALLDIR, "")

