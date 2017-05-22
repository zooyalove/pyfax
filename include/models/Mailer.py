import constant, func
from .htmlmail5 import HtmlMimeMail5

class Mailer(HtmlMimeMail5):
    def __init__(self):
        HtmlMimeMail5.__init__(self)

    def sendmail(self, to):
        self._send(to)

    def attach_file(self, file, altname=None):
        self._addAttachment(file, altname)

    def set_message(self, text):
        converted = text.replace('\n', '<br />')
        html = "<html><body>%s<br /><br />%s</body></html>" % (converted, constant.SYSTEM_EMAIL_SIG_HTML)

        text = "%s\n\n\n\n%s" % (text, constant.SYSTEM_EMAIL_SIG_TEXT)

        self.setText(func.decode_entity(text))
        self.setHTML(html)
        self.rebuild()

    def get_error(self):
        return self._errors
