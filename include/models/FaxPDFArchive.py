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

    def get_fid(self):
        pass

    def set_note(self, description, category, userid):
        pass
