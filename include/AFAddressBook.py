from pymongo import MongoClient

class AFAddressBook(object):
    def __init__(self):
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

    def get_error(self):
        pass
