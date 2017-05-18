from . import HtmlMimeMail5

class Mailer(HtmlMimeMail5):
    def __init__(self):
        super(HtmlMimeMail5, self).__init__()
