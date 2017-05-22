import abc, base64, re, hashlib, uuid, time
from os import path

import func


CRLF = None
MAIL_MIMEPART_CRLF = None


class Attachment(object):
    def __init__(self, data, name, content_type, encoding):
        self.data = data
        self.name = name
        self.content_type = content_type
        self.encoding = encoding


class FileAttachment(Attachment):
    def __init__(self, filename, content_type='application/octet-stream', altName=None, encoding=None):
        encoding = Base64Encoding() if encoding is None else encoding

        if not altName:
            altName = path.basename(filename)

        Attachment.__init__(self, func.file_get_contents(filename), altName, content_type, encoding)


class StringAttachment(Attachment):
    def __init__(self, data, name='', content_type='application/octet-stream', encoding=None):
        self.cid = None
        encoding = Base64Encoding() if encoding is None else encoding

        Attachment.__init__(self, data, name, content_type, encoding)


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

        self.__build_params = {'html_encoding': Base64Encoding(),
                               'text_encoding': Base64Encoding(),
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

    def setCRLF(self, crlf='\n'):
        global CRLF, MAIL_MIMEPART_CRLF

        if CRLF is None:
            CRLF = crlf

        if MAIL_MIMEPART_CRLF is None:
            MAIL_MIMEPART_CRLF = crlf

    def setSMTPParams(self, host=None, port=None, helo=None, auth=None, user=None, password=None):
        pass

    def setSendmailPath(self, spath):
        self.__sendmail_path = spath

    def setTextEncoding(self, encoding):
        self.__build_params['text_encoding'] = encoding

    def setHTMLEncoding(self, encoding):
        self.__build_params['html_encoding'] = encoding

    def setTextCharset(self, charset='ISO-8859-1'):
        self.__build_params['text_charset'] = charset

    def setHTMLCharset(self, charset='ISO-8859-1'):
        self.__build_params['html_charset'] = charset

    def setHeadCharset(self, charset='ISO-8859-1'):
        self.__build_params['head_charset'] = charset

    def setTextWrap(self, count=998):
        self.__build_params['text_wrap'] = count

    def setHeader(self, name, value):
        self.__headers[name] = value

    def setSubject(self, subject):
        self.__headers['Subject'] = subject

    def setFrom(self, from_email):
        self.__headers['From'] = from_email

    def setPriority(self, priority='normal'):
        p = priority.lower()
        if p in ['high', '1']:
            self.__headers['X-Priority'] = '1'
            self.__headers['X-MSMail-Priority'] = 'High'
        elif p in ['normal', '3']:
            self.__headers['X-Priority'] = '3'
            self.__headers['X-MSMail-Priority'] = 'Normal'
        elif p in ['low', '5']:
            self.__headers['X-Priority'] = '5'
            self.__headers['X-MSMail-Priority'] = 'Low'
        else:
            pass

    def setReturnPath(self, return_path):
        self.__return_path = return_path

    def setCc(self, cc):
        self.__headers['Cc'] = cc

    def setBcc(self, bcc):
        self.__headers['Bcc'] = bcc

    def setText(self, text):
        self.__text = text

    def setHTML(self, html, images_dir=None):
        self.__html = html

        if images_dir:
            self.findHtmlImages(images_dir)

    def rebuild(self):
        self.__is_built = False

    def findHtmlImages(self, images_dir):
        extensions = self.__image_types.keys()
        html_images = []

        match = re.match(r'(?:"|\'){[^"\']+\.(%s))(?:"|\')' % '|'.join(extensions), self.__html, re.U|re.I)
        groups = match.groups()

        for m in groups:
            if path.exists(images_dir + m):
                html_images.append(m)
                self.__html = self.__html.replace(m , path.basename(m))

        if not html_images:
            html_images = list(set(html_images))
            html_images.sort()

            for img in html_images:
                image = func.file_get_contents(images_dir+img)
                if image:
                    ext = re.sub(r"#^.*\.(\w{3,4})$#", r'"\1".lower()', img, re.I)
                    content_type = self.__image_types[ext]
                    self.addEmbeddedImage(StringEmbeddedImage(image, path.basename(img), content_type))

    def addEmbeddedImage(self, embedded_image):
        embedded_image.cid = hashlib.md5(uuid.uuid1(int(time.time())))
        self.__html_images.append(embedded_image)

    def addAttachment(self, attachment):
        self.__attachments.append(attachment)

    def addTextPart(self, message):
        params = {}
        params['content_type'] = 'text/plain'
        params['encoding'] = self.__build_params['text_encoding'].get_type()
        params['charset'] = self.__build_params['text_charset']

        if message:
            message.addSubpart()
