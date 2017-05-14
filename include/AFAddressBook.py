from MongoDB import MongoDB


class AFAddressBook(MongoDB):

    def __init__(self):
        super(MongoDB, self).__init__()

        self._error = ""

    def create(self, companyname):
        pass

    def loadbycid(self, cid):
        pass

    def get_companies(self, with_reserved=False):
        pass

    def search_companies(self, query):
        pass

    def totalfaxes(self, f, t):
        pass

    def get_companyid(self):
        pass

    def set_company(self, companyname):
        pass

    def delete_cid(self, cid):
        pass

    def has_fax2email(self):
        pass

    def get_company(self):
        pass

    def load_vals(self, data):
        pass

    def create_faxnumid(self, faxnumber):
        pass

    def delete_companyfaxids(self, cid):
        pass

    def delete_faxnumid(self, abookfax_id):
        pass

    def loadbyfaxnumid(self, abookfax_id):
        pass

    def loadbyfaxnum(self, faxnumber, mult):
        pass

    def reassign(self, newcid):
        pass
