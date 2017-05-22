from . import MongoDB


class AFUserAccount(MongoDB):
    def __init__(self):
        super(MongoDB, self).__init__()

        self.username = ''
        self.email = ''

    def get_uid(self):
        pass

    def loadbyemail(self, mailaddr):
        pass

    def load_username(self, owner):
        pass
