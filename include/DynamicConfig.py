import pymongo
from pymongo import MongoClient

class DynamicConfig(object):
    """DynamicConfig class
    """
    def __init__(self):
        self._client = MongoClient('localhost', 27017)
        self._db = self._client['zyapp']
        self._collection = self._db['dynconfs']

        self.dynconf_id = None
        self.device = None
        self.callid = None
        self.error = None

    def __del__(self):
        self.dynconf_id = None
        self.device = None
        self.callid = None
        self.error = None

        self._collection = None
        self._db = None
        self._client.close()

    def get_dynconf_id(self):
        """get_dynconf_id() -> ObjectId"""
        return self.dynconf_id

    def get_device(self):
        """get_device() -> string"""
        return self.device

    def get_callid(self):
        """get_callid() -> string"""
        return self.callid

    def get_error(self):
        """get_error() -> string"""
        return self.error

    def lookup(self, device, callid):
        """lookup(device, callid) -> Boolean"""
        docs = self._collection.find({"callid": callid})
        if docs:
            for row in docs:
                if not row['device'] or row['device'] == device:
                    return True
        else:
            return False

    def list_rules(self):
        """list_rules() -> Cursor"""
        return self._collection.find({}, projection={'_id': True, 'device': True, 'callid': True}, sort=('callid', pymongo.ASCENDING))

    def remove(self):
        pass

    def create(self, device, callid):
        self.callid = callid
        self.device = device
        rule = {'$and': [{'callid': callid}, {'device': device}]}

        if self._collection.find(rule):
            self.error = "Rule exists"
            return False

        result = self._collection.insert_one({'callid': callid, 'device': device})
        if result:
            self.dynconf_id = result.inserted_id
            return True

        self.error = "Rule not created"
        return False

    def load_rule(self, id):
        if not id:
            self.error = "DynConf not selected"
            return False

        data = self._collection.find_one({'id': id})
        if data:
            self.dynconf_id = data['_id']
            self.device = data['device']
            self.callid = data['callid']
            return True

        self.error = "Rule" + id + " doesn't exist"
        return False

    def save_rule(self, device, callid):
        if not self.dynconf_id:
            self.error = "DynConf not loaded"
            return False

        self.device = device
        self.callid = callid

        return self._collection.update
