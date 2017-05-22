from os import path


INSTALLDIR = path.realpath(path.dirname(__file__) + path.pathsep + '..' + path.pathsep)

BINARYDIR = "/usr/bin"

HYLAFAX_PREFIX = "/usr"

HYLASPOOL = "/var/spool/hylafax"

HYLATIFF2PS = False

ENABLE_DID_ROUTING = False

ADMIN_EMAIL = 'root@localhost'

COVERPAGE_FILE = 'cover.ps'

FAXMAILUSER = "faxmail"

WWWUSER = "apache"

EMAIL_DATE_FORMAT = "%d.%m.%Y %H:%M"

MAX_UPLOAD_SIZE = '5M'
MIN_PASSWD_SIZE = 8

PAPERSIZE = 'a4'

# tiff
TIFFCP = path.join(BINARYDIR, 'tiffcp')
TIFFCPG4 = TIFFCP + ' -c g4'
TIFFPS = path.join(BINARYDIR, 'tiff2ps') + ' -2ap'
TIFFSPLIT = path.join(BINARYDIR, 'tiffsplit')

TIFF_TO_G4 = False

# imagemagick
CONVERT = path.join(BINARYDIR, 'convert')

# netpbm
PNMSCALE = path.join(BINARYDIR, 'pnmscale')
PNMDEPTH = path.join(BINARYDIR, 'pnmdepth')
PPMTOGIF = path.join(BINARYDIR, 'ppmtogif')
PNMQUANT = path.join(BINARYDIR, 'pnmquant')

# psresize
PSRESIZE = path.join(BINARYDIR, 'psresize')

DPI = 92
DPIS = 200

GS = path.join(BINARYDIR, 'gs')
GSR = GS + " -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibility=1.4 -sPAPERSIZE={0}".format(PAPERSIZE)
GSN = GS + " -q -dNOPAUSE -sPAPERSIZE={0} -sDEVICE=pnm -r{1}x{1}".format(PAPERSIZE, DPI)
GSN2 = GS + " -q -dNOPAUSE -sPAPERSIZE={0} -sDEVICE=pnm".format(PAPERSIZE)
GSTIFF = GS + " -sDEVICE=tiffg4 -r{1}x{1} -dNOPAUSE -sPAPERSIZE={0}".format(PAPERSIZE, DPIS)
GSCMD = GS + " -dCompatibilityLevel=1.4 -dSAFER -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=%s -sPAPERSIZE=" + PAPERSIZE + " -f %s >/dev/null 2>/dev/null"

THUMBNAIL = 'thumb.gif'
NOTHUMB = 'images/nothumb.gif'
PDFNAME = 'fax.pdf'
TIFFNAME = 'fax.tif'
PREVIMG = 'prev'
PREVIMGSFX = '.gif'

SENDFAXFILETYPES = "PostScript (.ps), PDF (.pdf), TIFF (.tif), Text (.txt)"
CONTACTFILETYPES = "vCard (.vcf)"

PREV_TN = 80
PREV_SP = 750

NOTHUMBIMG = path.join(INSTALLDIR, NOTHUMB)

ARCHIVE = path.join(INSTALLDIR, 'faxes', 'recvd')
ARCHIVE_SENT = path.join(INSTALLDIR, 'faxes', 'sent')
TMPDIR = path.join(INSTALLDIR, 'tmp')
PHONEBOOK = path.join(INSTALLDIR, 'pbook.phb')
FAXCOVER = path.join(INSTALLDIR, 'include', 'faxcover.py')

# email configure
SYSTEM_EMAIL_SIG_HTML = "<a href='http://www.avantfax.com/'>AvantFAX</a>"
SYSTEM_EMAIL_SIG_TEXT = "www.AvantFAX.com"

USE_SMTPSERVER = False
SMTP_SERVER = 'localhost'
SMTP_PORT = 25
SMTP_AUTH = False
SMTP_USERNAME = ''
SMTP_PASSWORD = ''

NOTIFY_INCLUDE_PDF = False
NOTIFY_ON_SUCCESS = True
