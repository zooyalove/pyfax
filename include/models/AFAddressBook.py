from . import MongoDB


class AFAddressBook(MongoDB):

    def __init__(self):
        super(MongoDB, self).__init__()

        # private
        # SQL Table
        self._collection = self._db['addressbooks']
        self.__addressbookfax = self._db['addressbookfaxs']
        self.__addressbookemail = self._db['addressbookemails']

        # protected
        self._abook_id = None
        self._company = None

        self._email_array = []
        self._fax_array = {}


    def create(self, companyname):
        pass

    def create_faxnumid(self, faxnumber):
        pass

    def delete_companyfaxids(self, cid):
        pass

    def delete_faxnumid(self, abookfax_id):
        pass

    def totalfaxes(self, f, t):
        pass

    def get_companyid(self):
        pass

    def set_company(self, companyname):
        pass

    def get_company(self):
        pass

    def get_companies(self, with_reserved=False):
        pass

    def get_faxnums(self):
        if not self._abook_id:
            self._error = "No abook_id loaded"
            return None

        return self.__addressbookfax.find({'abook_id': self._abook_id})

    def get_faxnumber(self):
        if not self._fax_array.get('abookfax_id', None):
            self._error = "No abook_id loaded"
            return False

        return self._fax_array['faxnumber']

    def get_description(self):
        if not self._fax_array.get('abookfax_id', None):
            self._error = "No abook_id loaded"
            return False

        return self._fax_array.get('description', None)

    def get_category(self):
        if not self._fax_array.get('abookfax_id', None):
            self._error = "No abook_id loaded"
            return False

        return self._fax_array.get('faxcatid', None)

    def get_printer(self):
        if not self._fax_array.get('abookfax_id', None):
            self._error = "No abook_id loaded"
            return False

        return self._fax_array.get('printer', None)

    def get_faxnumid(self):
        if not self._fax_array.get('abookfax_id', None):
            self._error = "No abook_id loaded"
            return False

        return self._fax_array['abookfax_id']

    def get_email(self):
        if not self._fax_array.get('abookfax_id', None):
            self._error = "No abook_id loaded"
            return False

        return self._fax_array.get('email', None)

    def get_faxfrom(self):
        if not self._fax_array.get('abookfax_id', None):
            self._error = "No abook_id loaded"
            return False

        return self._fax_array.get('faxfrom', None)

    def get_faxto(self):
        if not self._fax_array.get('abookfax_id', None):
            self._error = "No abook_id loaded"
            return False

        return self._fax_array.get('faxto', None)

    def get_to_person(self):
        if not self._fax_array.get('abookfax_id', None):
            self._error = "No abook_id loaded"
            return False

        return self._fax_array.get('to_person', None)

    def get_to_location(self):
        if not self._fax_array.get('abookfax_id', None):
            self._error = "No abook_id loaded"
            return False

        return self._fax_array.get('to_location', None)

    def get_to_voicenumber(self):
        if not self._fax_array.get('abookfax_id', None):
            self._error = "No abook_id loaded"
            return False

        return self._fax_array.get('to_voicenumber', None)

    def delete_cid(self, cid):
        pass

    def has_fax2email(self):
        pass

    def load_vals(self, data):
        pass

    def loadbyfaxnumid(self, abookfax_id):
        pass

    def loadbyfaxnum(self, faxnumber, mult):
        pass

    def loadbycid(self, cid):
        pass

    def search_companies(self, query):
        pass

    def reassign(self, newcid):
        pass
