import pymongo

from . import MongoDB


class DynamicConfig(MongoDB):
    """DynamicConfig class
    """
    def __init__(self):
        super(MongoDB, self).__init__()

        self._collection = self._db['dynconfs']

        self.dynconf_id = None
        self.device = None
        self.callid = None

    def close(self):
        self.dynconf_id = None
        self.device = None
        self.callid = None

    def get_dynconf_id(self):
        """get_dynconf_id() -> ObjectId"""
        return self.dynconf_id

    def get_device(self):
        """get_device() -> string"""
        return self.device

    def get_callid(self):
        """get_callid() -> string"""
        return self.callid

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

    def remove(self, dc_id):
        res = self._collection.delete_one({'_id': dc_id})
        if res.deleted_count > 0:
            return True
        return False

    def create(self, device, callid):
        self.callid = callid
        self.device = device
        rule = {'$and': [{'callid': callid}, {'device': device}]}

        if self._collection.find(rule):
            self.set_error("Rule exists")
            return False

        result = self._collection.insert_one({'callid': callid, 'device': device})
        if result:
            self.dynconf_id = result.inserted_id
            return True

        self.set_error("Rule not created")
        return False

    def load_rule(self, dc_id):
        if not dc_id:
            self.set_error("DynConf not selected")
            return False

        data = self._collection.find_one({'_id': dc_id})
        if data:
            self.dynconf_id = data['_id']
            self.device = data['device']
            self.callid = data['callid']
            return True

        self.set_error("Rule" + dc_id + " doesn't exist")
        return False

    def save_rule(self, device, callid):
        if not self.dynconf_id:
            self.set_error("DynConf not loaded")
            return False

        self.device = device
        self.callid = callid

        return self._collection.update_one({'_id': self.dynconf_id}, {'device': device, 'callid': callid})
