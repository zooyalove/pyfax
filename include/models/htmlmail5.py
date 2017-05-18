import abc, base64
from os import path


import func


CRLF = None
MAIL_MIMEPART_CRLF = None


class Attachment(object):
    def __init__(self, data, name, contentType, encoding):
        self.data = data
        self.name = name
        self.contentType = contentType
        self.encoding = encoding


class FileAttachment(Attachment):
    def __init__(self, filename, contentType='application/octet-stream', altName=None, encoding=None):
        encoding = Base64Encoding() if encoding is None else encoding

        if not altName:
            altName = path.basename(filename)

        super(Attachment, self).__init__(open(filename).read(1000), altName, contentType, encoding)


class StringAttachment(Attachment):
    def __init__(self, data, name='', contentType='application/octet-stream', encoding=None):
        encoding = Base64Encoding() if encoding is None else encoding

        super(Attachment, self).__init__(data, name, contentType, encoding)


class FileEmbeddedImage(FileAttachment):
    pass


class StringEmbeddedImage(StringAttachment):
    pass


class iEncoding(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def encode(self, inp):
        raise NotImplementedError('users must define encode to use this base class')

    @abc.abstractmethod
    def get_type(self):
        raise NotImplementedError('users must define get_type to use this base class')


class Base64Encoding(iEncoding):
    def encode(self, inp):
        global CRLF, MAIL_MIMEPART_CRLF

        return func.chunk_split(base64.b64encode(inp), MAIL_MIMEPART_CRLF if MAIL_MIMEPART_CRLF else '\r\n').rstrip()

    def get_type(self):
        return 'base64'


class QPrintEncoding(iEncoding):
    def encode(self, inp):
        # inp = re.sub(r"([^\x20\x21-\x3C\x3E-\x7E\x0A\x0D])")
        pass

    def get_type(self):
        return 'quoted-printable'


class SevenBitEncoding(iEncoding):
    def encode(self, inp):
        return inp

    def get_type(self):
        return '7bit'


class EightBitEncoding(iEncoding):
    def encode(self, inp):
        return inp

    def get_type(self):
        return '8bit'


class HtmlMimeMail5(object):
    def __init__(self):
        # private property
        self.__html = None
        self.__text = ""
        self.__output = None
        self.__html_images = []

        self.__image_types = {'gif': 'image/gif',
                              'jpg': 'image/jpeg',
                              'jpeg': 'image/jpeg',
                              'jpe': 'image/jpeg',
                              'bmp': 'image/bmp',
                              'png': 'image/png',
                              'tif': 'image/tiff',
                              'tiff': 'image/tiff',
                              'swf': 'application/x-shockwave-flash'}

        self.__build_params = {'html_encoding': base64,
                               'text_encoding': base64,
                               'html_charset': 'UTF-8',
                               'text_charset': 'UTF-8',
                               'head_charset': 'UTF-8',
                               'text_wrap': 998}

        self.__attachments = []

        helo = 'localhost'

        self.__smtp_params = {'host': 'localhost',
                              'port': 25,
                              'helo': helo,
                              'auth': False,
                              'username': '',
                              'password': ''}

        self.__headers = {'MIME-Version': '1.0', 'X-Mailer': 'AvantFAX 3'}

        self.__is_built = False
        self.__return_path = None
        self.__sendmail_path = "/usr/lib/sendmail"

        # protected property
        self._errors = ""

