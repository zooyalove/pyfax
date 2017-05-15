from os import path


INSTALLDIR = path.realpath(path.dirname(__file__) + path.pathsep + '..' + path.pathsep)

BINARYDIR = "/usr/bin"

HYLAFAX_PREFIX = "/usr"

HYLASPOOL = "/var/spool/hylafax"

HYLATIFF2PS = False

TMPDIR = path.join(INSTALLDIR, 'tmp')

ADMIN_EMAIL = 'root@localhost'

COVERPAGE_FILE = 'cover.ps'

FAXMAILUSER = "faxmail"

WWWUSER = "apache"

EMAIL_DATE_FORMAT = "%d.%m.%Y %H:%M"

SENDFAXFILETYPES = "PostScript (.ps), PDF (.pdf), TIFF (.tif), Text (.txt)"

CONTACTFILETYPES = "vCard (.vcf)"

MAX_UPLOAD_SIZE = '5M'

MIN_PASSWD_SIZE = 8

TIFFPS = path.join(BINARYDIR, 'tiff2ps') + ' -2ap'

PAPERSIZE = 'a4'

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
