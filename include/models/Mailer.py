from .htmlmail5 import HtmlMimeMail5

class Mailer(HtmlMimeMail5):
    def __init__(self):
        HtmlMimeMail5.__init__(self)
