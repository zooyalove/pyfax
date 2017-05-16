from pymongo import MongoClient


class MongoDB(object):
    def __init__(self):
        self._client = MongoClient('localhost', 27017)
        self._db = self._client['zyapp']
        self._error = ""

    def __del__(self):
        self._db = None
        self._client.close()
        self._error = None

        self.close()

    def close(self):
        pass

    def get_error(self):
        return self._error
