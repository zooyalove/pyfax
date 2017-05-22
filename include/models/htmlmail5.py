# -*- coding:utf-8 -*-

import mimetypes
from os import path

import smtplib
from email.header import Header
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email import encoders


class HtmlMimeMail5(object):
    def __init__(self):
        # private property
        self.__html = None
        self.__text = None
        self.__output = MIMEMultipart()

        self.__attachments = []

        self.__msg_users = {
            'from': '',
            'to': '',
            'cc': '',
            'bcc': ''
        }
        self.__smtp_params = {'host': 'localhost',
                              'port': 25,
                              'auth': False,
                              'username': '',
                              'password': ''}

        self.__is_built = False

        # protected property
        self._errors = ""


    def setSMTPParams(self, host='localhost', port=25, auth=False, user='', password=''):
        self.__smtp_params = {'host': host,
                            'port': port,
                            'auth': auth,
                            'username': user,
                            'password': password}

    def setHeader(self, name, value):
        self.__output[name] = value

    def setSubject(self, subject):
        self.__output['Subject'] = Header(s=subject, charset='utf-8')

    def setFrom(self, from_email):
        self.__msg_users['from'] = from_email
        self.__output['From'] = from_email

    def setCc(self, cc_users):
        self.__msg_users['cc'] = cc_users
        self.__output['Cc'] = ', '.join(cc_users)

    def setBcc(self, bcc_users):
        self.__msg_users['bcc'] = bcc_users
        self.__output['Bcc'] = ', '.join(bcc_users)

    def setText(self, text):
        self.__text = MIMEText(text, _charset='utf=8')

    def setHTML(self, html):
        self.__html = MIMEText(html, 'html', _charset='utf-8')

    def rebuild(self):
        self.__is_built = False

    # def findHtmlImages(self, images_dir):
    #     extensions = self.__image_types.keys()
    #     html_images = []
    #
    #     match = re.match(r'(?:"|\'){[^"\']+\.(%s))(?:"|\')' % '|'.join(extensions), self.__html, re.U|re.I)
    #     groups = match.groups()
    #
    #     for m in groups:
    #         if path.exists(images_dir + m):
    #             html_images.append(m)
    #             self.__html = self.__html.replace(m , path.basename(m))
    #
    #     if not html_images:
    #         html_images = list(set(html_images))
    #         html_images.sort()
    #
    #         for img in html_images:
    #             image = func.file_get_contents(images_dir+img)
    #             if image:
    #                 ext = re.sub(r"#^.*\.(\w{3,4})$#", r'"\1".lower()', img, re.I)
    #                 content_type = self.__image_types[ext]
    #                 self.addEmbeddedImage(StringEmbeddedImage(image, path.basename(img), content_type))
    #
    # def addEmbeddedImage(self, embedded_image):
    #     embedded_image.cid = hashlib.md5(uuid.uuid1(int(time.time())))
    #     self.__html_images.append(embedded_image)

    def _addAttachment(self, filename, altname=None):
        if not path.isfile(filename) or filename is None:
            return False

        ctype, encoding = mimetypes.guess_type(filename)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'

        maintype, subtype = ctype.split('/', 1)

        if maintype == 'text':
            with open(filename) as fp:
                msg = MIMEText(fp.read(), _subtype=subtype)
        elif maintype == 'image':
            with open(filename, 'rb') as fp:
                msg = MIMEImage(fp.read(), _subtype=subtype)
        elif maintype == 'audio':
            with open(filename, 'rb') as fp:
                msg = MIMEAudio(fp.read(), _subtype=subtype)
        else:
            with open(filename, 'rb') as fp:
                msg = MIMEBase(maintype, subtype)
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)

        msg.add_header('Content-Disposition', 'attachment; filename="%s"' % (path.basename(filename) if altname is None else altname))

        self.__attachments.append(msg)

        return True

    def _build(self, to_email):
        if self.__is_built:
            return True

        self.__output['To'] = to_email
        self.__output['Date'] = formatdate(localtime=True)

        if len(self.__attachments) > 0:
            for attachment in self.__attachments:
                self.__output.attach(attachment)

        self.__is_built = True
        return True

    def _send(self, to):
        self._build(to)

        s = smtplib.SMTP(self.__smtp_params['host'], self.__smtp_params['port'])

        if self.__smtp_params['host'] != 'localhost':
            if not self.__smtp_params['username'] or not self.__smtp_params['password']:
                self._errors = "SMTP 유저아이디 혹은 SMTP 패스워드가 설정되어 있지 않습니다."
                s.close()
                return False

            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(self.__smtp_params['username'], self.__smtp_params['password'])

        to_user = to + self.__msg_users['cc']
        s.sendmail(self.__msg_users['from'], to_user, self.__output.as_string())
        s.close()
        return True
