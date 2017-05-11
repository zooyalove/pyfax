from pymongo import MongoClient

class DynamicConfig(object):
    def __init__(self):
        self._client = MongoClient('localhost', 27017)
        self._db = self._client['zyapp']
        self._collection = self._db['dynconfs']

        self.dynconf_id = None
        self.device = None
        self.callid = None
        self.error = None

    def lookup(self, pDevice, pCallid):
        docs = self._collection.find({"callid": pCallid})
        if docs:
            for row in docs:
                if not row['device'] or row['device'] == pDevice:
                    return True
        else:
            return False
