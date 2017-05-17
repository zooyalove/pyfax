from . import MongoDB


class FaxPDFArchive(MongoDB):
    def __init__(self):
        super(MongoDB, self).__init__()

        # private
        self.__archive_results = None
        self.__sqlroutes = None
        self.__debug = True

        # protected
        self._thumbnail = None
        self._tiffpath = None
        self._pdfpath = None
        self._faximages = None
        self._m_archstamp = None
        self._m_lastmoddate = None
        self._m_lastoperation = None

        self._collection = self._db['faxarchives']
        self._dbdata = {}

    def get_userid(self):
        if not self._dbdata.get('fid', False):
            self._error = "No fid loaded"
            return False

        return self._dbdata['userid']

    def get_fid(self):
        return self._dbdata.get('fid', None)

    def get_description(self):
        return self._dbdata.get('description', None)

    def get_lastmoduser(self):
        return self._dbdata.get('lastmoduser', None)

    def get_faxnumid(self):
        return self._dbdata.get('faxnumid', None)

    def get_origfaxnum(self):
        return self._dbdata.get('origfaxnum', None)

    def get_pages(self):
        return self._dbdata.get('pages', None)

    def get_inbox(self):
        return self._dbdata.get('inbox', None)

    def get_companyid(self):
        return self._dbdata.get('companyid', None)

    def get_didr_id(self):
        return self._dbdata.get('didr_id', None)

    def get_modemdev(self):
        return self._dbdata.get('modemdev', None)

    def get_tiffpath(self):
        return self._tiffpath

    def get_pdfpath(self):
        return self._pdfpath

    def get_thumbnail(self):
        return self._thumbnail

    def get_faximages(self):
        return self._faximages

    def get_archstamp(self):
        return self._m_archstamp

    def get_lastmoddate(self):
        return self._m_lastmoddate

    def set_note(self, description, category, userid):
        pass
