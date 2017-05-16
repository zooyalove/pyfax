import constant


LANG = {
    'ISO': 'charset=UTF-8',

    'DIRECTION': 'ltr',

    'YES': 'Yes',
    'NO': 'No',

    'DATE': 'Date',
    'FROM': 'From',
    'TO': 'To',

    'DATE_START': 'Start Date',
    'DATE_END': 'End Date',

    'TO_PERSON': 'To person',
    'TO_COMPANY': 'To company',
    'TO_LOCATION': 'To location',
    'TO_VOICENUMBER': 'To voice number',

    'MY_COMPANY': 'Company',
    'MY_LOCATION': 'Location',
    'MY_VOICENUMBER': 'Voice number',
    'MY_FAXNUMBER': 'Fax number',
    
    'VIEW_FAX': 'View Fax',
    'ROTATE_FAX': 'Rotate Fax',
    'DOWNLOAD_PDF': 'Download PDF',
    'DOWNLOAD_TIFF': 'Download TIFF',
    'EMAIL_PDF': 'Email PDF',
    'ADD_NOTE_FAX': 'Add a note',
    'ARCHIVE_FAX': 'Move to Archive',
    'DELETE_FAX': 'Permanently delete',
    
    'DELETE_CONFIRM': 'Please confirm you want to delete this fax.',
    
    'ASSIGN_CNAME': 'Assign a company name',
    'ASSIGN_MISSING': 'You must enter a company name',
    'ASSIGN_NOTE': 'Modify this fax\'s note / description',
    'ASSIGN_NOTE_SAVED': 'Note / description saved.',
    'ASSIGN_OK': 'Company name was successfully assigned.',
    'FAXES': 'faxes',
    
    'NAME': 'Name',
    'DESCRIPTION': 'Description',
    'SAVE': 'Save',
    'DELETE': 'Delete',
    'CANCEL': 'Cancel',
    'CREATE': 'Create',
    'EMAIL': 'Email',
    'SELECT': 'Select',
    'CONTACT_SAVED': 'Contact details saved',
    'CONTACT_DELETED': 'Contact deleted',
    'RUBRICA_SAVED': 'Company details saved',
    'RUBRICA_DELETED': 'Company deleted',
    
    'FAX_FILES': 'Select the files to FAX',
    'FAX_DEST': 'Destination fax numbers',
    'FAX_CPAGE': 'Use cover page',
    'FAX_REGARDING': 'Regarding',
    'FAX_COMMENTS': 'Comments',
    'FAX_FILETYPES': 'You can attach the following file types: ' + constant.SENDFAXFILETYPES,
    'FAX_FILE_MISSING': 'You must choose a file to fax',
    'FAX_DEST_MISSING': 'You must enter the destination fax numbers',
    'FAX_SUBMITTED': 'Your fax has been successfully queued to be faxed.<br />You will receive a confirmation email once the fax is sent.',
    'FAX_FILESIZE': 'File size is over the limit.',
    'FAX_MAXSIZE': 'Max file size is ' + constant.MAX_UPLOAD_SIZE,
    'NOTIFY_REQUEUE': 'Notify on requeue',
    
    'FUPLOAD_NO_FILE': 'No file uploaded',
    'FUPLOAD_NOT_ALLOWED': 'File type is unauthorized',
    'FUPLOAD_OVER_LIMIT': 'File size is over the limit',
    'FUPLOAD_OVER_LIMIT_INI': 'File size is over the limit (INI)',
    'FUPLOAD_OVER_LIMIT_FORM': 'File size is over the limit (FORM)',
    'FUPLOAD_NOT_COMPLETE': 'File not completely uploaded',
    'FUPLOAD_NO_TEMPDIR': 'No temporary directory',
    'FUPLOAD_CANT_WRITE': 'Can\'t write uploaded file',
    
    'YOUR_NAME': 'Your name',
    'UPDATE': 'Update',
    'USER_DETAILS_SAVED': 'User settings have been saved.',
    
    'LANGUAGE': 'Language',
    'EMAIL_SIG': 'E-mail signature',
    
    'NEXT_FAX': 'Next Fax',
    'PREV_FAX': 'Previous Fax',
    
    'LOGIN_TEXT': 'Enter your username and password to access the fax interface.',
    'LOGIN_DISABLED': 'Your account has been disabled.  Please contact the administrator.',
    'LOGIN_INCORRECT': 'Incorrect username or password.<br />Please try again.',
    'LOGIN_ALT_FAILED': 'Login failed for %s.  Ask your admin to verify that the account exists in AvantFAX.',
    'ACCESS_DENIED': 'Access denied',
    
    'USERNAME': 'username',
    'PASSWORD': 'password',
    'USER': 'User',
    'BUTTON_LOGIN': 'Login',
    'BUTTON_LOGOUT': 'Logout',
    'BUTTON_SETTINGS': 'Settings',
    
    'MENU_MENU': 'Menu',
    'MENU_INBOX': 'Inbox',
    'MENU_OUTBOX': 'Outbox',
    'MENU_SENDFAX': 'Send Fax',
    'MENU_ARCHIVE': 'Archive',
    'MENU_CONTACTS': 'Contacts',
    
    'SELECT_ALL_FAXES': 'Select All Faxes',
    'FAXES_PER_PAGE': 'faxes per page',
    'INBOX_SHOW': 'Inbox - show',
    'ARCHIVE_SHOW': 'Archive - show',
    
    'CONTACT_HEADER_EMAIL': 'Email',
    'CONTACT_HEADER_FAX': 'Fax',
    'CONTACT_HEADER_COMPANY': 'Company',
    'CONTACT_HEADER_NEWFAX': 'New fax number',
    'CONTACT_HEADER_FAXNUM': 'Fax number',
    'NEW_ENTRY': 'New entry',
    'UPLOAD_CONTACTS': 'Upload contacts file ' + constant.CONTACTFILETYPES,
    'CONTACTS_UPLOADED': 'Successfully uploaded %d contacts',
    'UPLOAD_BUTTON': 'Upload',
    
    'SEND_EMAIL_HEADER': 'Forward fax via email',
    'EMAIL_RECIPIENTS': 'Email recipients',
    'EMAIL_CCRECIPIENTS': 'Email recipients (CC)',
    'EMAIL_BCCRECIPIENTS': 'Email recipients (BCC)',
    'MESSAGE_PROMPT': 'Email message',
    'BUTTON_SEND': 'Send',
    'SUBJECT': 'Subject',
    'PDF_FILENAME': 'PDF file name',
    
    'EMAIL_SUCCESS': 'The email was sent successfully.',
    'EMAIL_FAILURE': 'The email failed to send.',
    
    'PN_PAGE': 'Page',
    'PN_PAGE_UP': 'Page Up',
    'PN_PAGE_DN': 'Page Down',
    'PN_PAGES': 'Pages',
    'PN_OF': 'of',
    'NUM_DIALS': 'Dials',
    'KILL_JOB': 'Kill job',
    
    'PROMPT_CLOSEWINDOW': 'Close Window',
    
    'LAST_UPDATED': 'Last Updated',
    'BACK': 'Back',
    'EDIT': 'Edit',
    'ADD': 'Add',
    'WARNCAT': 'Please select a category',
    'TITLE': 'Title',
    'CATEGORY': 'Category',
    'CATEGORY_NAME': 'Category name',
    
    'LAST_MOD': 'Last modified by',

    'MONTHS': ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],

    'ERROR_PASS': 'Sorry, no corresponding user was found.',

    'NEWPASS_MSG': """he user account %s has this email associated with it.  A web user from %s has just requested that a new password be sent.
    
    Your New Password is: %s
    
    If this was an error just login with your new password and then change your password to what you would like it to be.""",
    
    'ADMIN_NEWPASS_MSG': 'The admin account password was reset to:\n\t%s\n by a user from %s',
    
    'REGWARN_MAIL': 'Please enter a valid e-mail address.',
    'REGWARN_PASS': 'Please enter a valid password.  No spaces, more than ".MIN_PASSWD_SIZE." characters and contain 0-9, a-z, A-Z.',
    'REGWARN_VPASS2': 'Password and verification do not match, please try again.',
    'REGWARN_USERNAME_INUSE': 'This username already in use. Please try another.',
    
    'USER_UPDATE_ERROR': 'Error updating account',
    'PASS_TOO_LONG': 'Password too long',
    'PASS_TOO_SHORT': 'Password too short',
    'PASS_ALREADY_USED': 'This password has already been used.  Please create a new one.',
    'PASS_ERROR_CHANGING': 'Error changing password for',
    'PASS_ERROR_RESETTING': 'Error resetting password for',
    'ERROR_SENDING_EMAIL': 'Email failed to send',
    'REGWARN_USERNAME': 'Non-alphanumeric characters are not allowed in username.',
    'REGWARN_NOUSERNAME': 'You must enter a username',
    'REGWARN_MAIL_EXISTS': 'Email address is already in use.',
    
    'LOST_PASSWORD': 'Lost your Password?',
    
    'PROMPT_UNAME': 'Username',
    'PROMPT_PASSWORD': 'Password',
    'PROMPT_CAN_REUSE_PWD': 'User can reuse old passwords',
    'REPLY_TO_FAX': 'Reply to FAX',
    'REPLY_TO_FAX_TIP': 'The original fax will be the first document faxed after the coverpage',
    'PROMPT_EMAIL': 'E-mail Address',
    'BUTTON_SEND_PASS': 'Send Password',
    'REGISTER_VPASS': 'Verify Password',
    'FIELDS_REQUIRED': 'Fields marked with an asterisk (*) are required.',
    
    'NEW_PASS_DESC': 'Please enter your e-mail address then click on the Send Password button.<br /><br />You will receive a new password shortly.<br /><br />Use this new password to access the site.<br /><br />',
    'NEW_ADMIN_PASS_DESC': 'Enter your username and e-mail address then click on the Send Password button.<br /><br />You will receive a new password shortly.<br /><br />',
    'RESETTING_PASSWORD': 'Your password will be sent to the given e-mail address.<br /><br />Once you have received your new password you can login in and change it.<br /><br />',
    
    'SEARCH_TITLE': 'Search',
    'KEYWORDS': 'Keywords',
    'COMPANY_SEARCH': 'Company search',
    'COMPANY_LIST': 'Company list',
    'SENT_RECVD': 'Sent / Received',
    'BOTH_SENT_RECVD': 'Both sent and received faxes',
    'ONLY_MY_SENT': 'Only sent faxes',
    'ONLY_RECVD': 'Only received faxes',
    'CONCLUSION': 'Total %d results found.',
    'NOKEYWORD': 'No results were found',
    
    'SEARCH_WHITEPAGES': 'Search the White Pages',
    
    'PWD_NEEDS_RESET': 'Your password must be changed before you can continue.',
    'PWD_REQUIREMENTS': 'Password must be at least ' + constant.MIN_PASSWD_SIZE + ' characters.',
    'OPASS': 'Old Password',
    'NPASS': 'New Password',
    'VPASS': 'Verify Password',
    'OPASS_WRONG': 'Old password is incorrect.',
    'NAME_MISSING': 'You must enter a name.',
    
    'MODIFY_FAXNUMS': 'Modify company fax numbers',
    'MODIFY_EMAILS': 'Modify your email address book',
    'TITLE_FAXNUMS': 'Fax Numbers',
    'TITLE_EMAILS': 'Email Addresses',
    
    'TITLE_DISTROLIST': 'Distribution Lists',
    'DISTROLIST_NAME': 'List name',
    'DISTROLIST_DELETE': 'Delete list',
    'DISTROLIST_CONFIRM_DELETE': 'Delete this distribution list?',
    'DISTROLIST_SAVENAME': 'Save list name',
    
    'CHANGES_SAVED': 'Changes saved',
    'DISTROLIST_DELETED': 'List deleted',
    'DISTROLIST_NOT_CREATED': 'List not created',
    'DISTROLIST_EXISTS': 'List already exists',
    'DISTROLIST_ENTER_LISTNAME': 'Enter a name for the list',
    'DISTROLIST_ADD': 'Add entries',
    'DISTROLIST_REMOVE': 'Remove entries',
    'DISTROLIST_REFRESH_LIST': 'Refresh List',
    
    'NEW_USER_MESSAGE_SUBJECT': 'New User Details',
    'NEW_USER_MESSAGE': """Hello %s,
    
    This email contains your username and password to log into AvantFAX (http://%s)
    
    Username - %s
    Password - %s
    
    Please do not respond to this message as it is automatically generated and is for information purposes only""",
    
    'DIDROUTE_EXISTS': 'Route already exists',
    'DIDROUTE_NOT_CREATED': 'Route was not created',
    'DIDROUTE_NO_ROUTES': 'No DID/DTMF Routes configured',
    'DIDROUTE_DOESNT_EXIST': 'Route %s does not exist',
    'ADMIN_PRINTER': 'Printer',
    'PRINT': 'Print',
    
    'ADMIN_DIDROUTE_CREATED': 'The route was created',
    'ADMIN_DIDROUTE_DELETED': 'The route was deleted',
    'ADMIN_DIDROUTE_UPDATED': 'The route was updated',
    'ADMIN_DIDROUTES': 'DID/DTMF Route groups',
    'DIDROUTE_ROUTECODE': 'DID/DTMF digits',
    'DIDROUTE_CATCHALL': 'Catch All',
    'ADMIN_CONFDIDROUTING': 'DID/DTMF Groups',
    'GROUP': 'Group',
    
    'USER_ANYMODEM': 'User can fax from any modem',
    
    'BARCODEROUTE_BARCODE': 'Barcode',
    'MISSING_BARCODE': 'Missing barcode',
    'ADMIN_BARCODEROUTE_DELETED': 'Barcode route deleted',
    'ADMIN_BARCODEROUTE_UPDATED': 'Barcode route updated',
    'ADMIN_BARCODEROUTE_CREATED': 'Barcode route created',
    'BARCODEROUTE_NOT_CREATED': 'Barcode route not created',
    'BARCODEROUTE_EXISTS': 'Barcode route exists',
    'BARCODEROUTE_NO_ROUTES': 'No barcode routes',
    'BARCODEROUTE_DOESNT_EXIST': 'Barcode route %s doesn\'t exist',
    
    'FAXCAT_NOT_CREATED': 'Fax category \'%s\' was not created',
    'FAXCAT_ALREADY_EXISTS': 'Fax category \'%s\' already exists',
    
    'FAX_FAILED': 'Problem sending the fax.',
    'FAX_WHY': {"done": 'Done',
        "format_failed": 'format failed',
        "no_formatter": 'no formatter',
        "poll_no_document": 'poll no document',
        "killed": 'killed',
        "rejected": 'rejected',
        "blocked": 'blocked',
        "removed": 'removed',
        "timedout": 'timed out',
        "poll_rejected": 'poll rejected',
        "poll_failed": 'poll failed',
        "requeued": 'requeued'},
    
    'COMPANY_EXISTS': 'Company name already exists',
    'FAXNUMID_NOT_CREATED': 'Could not create faxnumid',
    'NO_COMPANY_FOR_FAXNUM': 'No company for this fax number',
    'CANT_CHANGE_FAXNUM': 'You can\'t change an established fax number',
    
    'MODEM_EXISTS': 'Modem device already exists',
    'MODEM_NOT_CREATED': 'Modem device was not created',
    'NO_MODEMS_CONFIGURED': 'No modems configured',
    'MODEM_DOESNT_EXIST': 'Modem %s does not exist',
    
    'COVER_EXISTS': 'Cover page already exists',
    'COVER_NOT_CREATED': 'Cover page was not created',
    'NO_COVERS_CONFIGURED': 'No cover pages configured',
    'COVER_DOESNT_EXIST': 'Cover page %s does not exist',
    
    'ADMIN_FAXCAT_DELETED': 'The category was deleted',
    'ADMIN_FAXCAT_CREATED': 'The category was created',
    'ADMIN_FAXCAT_UPDATED': 'The category was updated',
    
    'ADMIN_MODEM_CREATED': 'The modem was created',
    'ADMIN_MODEM_DELETED': 'The modem was deleted',
    'ADMIN_MODEM_UPDATED': 'The modem was updated',
    
    'ADMIN_COVER_CREATED': 'The cover page was created',
    'ADMIN_COVER_DELETED': 'The cover page was deleted',
    'ADMIN_COVER_UPDATED': 'The cover page was updated',
    
    'FAXFREE': 'Idle',
    'FAXSEND': 'Sending a fax',
    'FAXRECV': 'Receiving a fax',
    'FAXRECVFROM': 'Receiving a fax from',
    
    'MODEM_DEVICE': 'Device',
    'MODEM_CONTACT': 'Contact',
    'MODEM_ALIAS': 'Alias',
    
    'COVER_FILE': 'File name',
    'COVER_TITLE': 'Coverpage Title',
    'SELECT_COVERPAGE': 'Select cover page',
    
    'MISSING_CATEGORY_NAME': 'You must enter a category name',
    'MISSING_DEVICE_NAME': 'You must enter a device name',
    'MISSING_ALIAS_NAME': 'You must enter an alias',
    'MISSING_CONTACT_NAME': 'You must enter a contact name',
    'MISSING_ROUTE': 'You must enter the DID/DTMF digits',
    
    'MISSING_FILE_NAME': 'You must enter a file name',
    'MISSING_TITLE_NAME': 'You must enter a title',
    
    'ADMIN_CONFIGURE': 'Configure...',
    'ADMIN_USERS': 'Users',
    'ADMIN_NEW_USER': 'New User',
    'ADMIN_EDIT_USER': 'Modify User',
    'ADMIN_DEL_USER': 'Delete User',
    'ADMIN_LAST_LOGIN': 'Last Login',
    'ADMIN_LAST_IP': 'Last IP',
    'ADMIN_USER_LIST': 'User List',
    'ADMIN_FAXCATS': 'Fax Categories',
    'ADMIN_CONFMODEMS': 'Modems',
    'ADMIN_CONFCOVERS': 'Cover Pages',
    
    'ADMIN_ROUTING_BY': 'Configure routing by...',
    'ADMIN_ROUTEBY_SENDER': 'Routing by Sender',
    'ADMIN_ROUTEBY_SENDER_SHORT': 'Sender',
    'ADMIN_ROUTEBY_BARCODE': 'Routing by Barcode',
    'ADMIN_ROUTEBY_BARCODE_SHORT': 'Barcode',
    'ADMIN_ROUTEBY_KEYWORD': 'Routing by Keyword',
    'ADMIN_ROUTEBY_KEYWORD_SHORT': 'Keyword',
    
    'ADMIN_DASHBOARD': 'Dashboard',
    'ADMIN_STATS': 'Statistics',
    'ADMIN_SYSLOGS': 'System Logs',
    'ADMIN_SYSFUNC': 'System Functions',
    'ADMIN_NOUSERS': 'No users created',
    'ADMIN_ACC_ENABLED': 'Account active',

    'ADMIN_PWDCYCLE': ['Password expiration cycle', 'Never', 'Every 3 Months', 'Every 6 Months'],
    'ADMIN_PWDEXP': 'Password expiration date',
    'SUPERUSER': 'Super user',
    'IS_ADMIN': 'Administrator',
    'USER_CANDEL': 'User can delete faxes',
    'ADMIN_FAXLINES': 'Viewable fax lines',
    'ADMIN_CATEGORIES': 'Viewable fax categories',
    'REBOOT': 'Reboot server',
    'SHUTDOWN': 'Shutdown server',
    'DOWNLOADARCHIVE': 'Download Archive',
    'DOWNLOADDB': 'Download Database',
    'PLSWAIT': 'Please wait',
    'LOGTEXT': 'Log information',
    'QUESTION_DELUSER': 'Are you sure you want to delete',
    
    'TSI_ID': 'TSI ID',
    'PRIORITY': 'Priority',
    'BLACKLIST': 'Blacklist',
    'MODIFY_FAXJOB': 'Modify Job',
    'NEW_DESTINATION': 'New Destination',
    'SCHEDULE_FAX': 'Schedule delivery',
    'FAX_NUMTRIES': 'Number of tries',
    'FAX_KILLTIME': 'Kill time',
    'NOW': 'Now',
    'MINUTES': 'Minutes',
    'HOURS': 'Hours',
    'DAYS': 'Days',
    
    'ADMIN_CONFDYNCONF': 'Black List',
    'DYNCONF_MISSING_CALLID': 'You must enter the CallID',
    'DYNCONF_NOT_CREATED': 'Rule not created',
    'DYNCONF_EXISTS': 'Rule exists',
    'DYNCONF_CALLID': 'Caller ID',
    'DYNCONF_CREATED': 'Rule created',
    'DYNCONF_DELETED': 'Rule deleted',
    'DYNCONF_UPDATED': 'Rule updated',
    'OPTIONS': 'Options',
    
    'MUST_CREATE_ROUTES': '<a href=\"conf_didroute.php\">You must first create a DID/DTMF group</a>',
    'MUST_CREATE_MODEMS': '<a href=\"conf_modems.php\">You must first create a modem</a>',
    'MUST_CREATE_CATEGORIES': '<a href=\"fax_categories.php\">You must first create a category</a>',
    
    'EXPLAIN_CATEGORIES': 'Categories are useful for organizing faxes in the AvantFAX Archive.  Normal users are limited to viewing the categories assigned to them.',
    'EXPLAIN_DYNCONF': 'HylaFAX\'s DynamicConfig and RejectCall features are used to reject fax transmissions from known offenders.  To add an entry to this Black List, enter the Caller ID of the sender you would like to block.  Optionally, you may select a device if you only want to block this sender on that device.',
    'EXPLAIN_DIDROUTE': 'DID/DTMF routing is used to route faxes sent to a hunt group.  HylaFAX must be properly configured for this to work.  An individual entry must be created for each hunt group you intend to use with AvantFAX.  The DID/DTMF digits field is for hunt group information as received by HylaFAX -- typically the last 3 or 4 digits or even 10 digits of the fax number. The Alias field is used to describe the location or purpose for the hunt group.  For example, Sales or Support for a fax line dedicated for those departments.  The Contact field is for an email address, and every fax that arrives for this group will be emailed to the Contact.  The Printer field specifies which CUPS/lpr printer to print the fax on.  Normal users can only view faxes from the hunt groups assigned to them.',
    'EXPLAIN_MODEMS': 'A Modem entry must be created for each modem device you intend to use with AvantFAX.  The Device field is for the name of the device as it is configured in HylaFAX (ie: ttyS0, ttyds01 or boston00). The Alias field is used to describe the location or purpose for the modem.  For example, Sales or Support for a fax line dedicated for those departments.  The Contact field is for an email address, and every fax that arrives on this modem will be emailed to the Contact.  The Printer field specifies which CUPS/lpr printer to print the fax on.  Normal users can only view faxes from the modems assigned to them.',
    'EXPLAIN_COVERS': 'A Cover Page entry must be created for each cover page you intend to use with AvantFAX.  The File field is for the name of the template file found in the images/ folder (ie: cover.ps, custom.ps, or mycover.html). The Title field is used to describe the cover page.  For example: Generic, Sales Dept, Accounting Dept.  Anyone can choose any of the cover pages defined here.',
    'EXPLAIN_FAX2EMAIL': 'Routing by Sender (formerly Fax2Email) is for routing individual fax numbers to a specific email address.  If you want the faxes sent from 18002125555 to be emailed to sales@yourcompany.com, you must select the company in the list on the left and enter the email address into the Email field.  The Company field allows you to modify the company name as displayed in the Address Book.  The Printer field specifies which CUPS/lpr printer to print the fax on.  Also, you may select a category to automatically categorizing the fax.',
    'EXPLAIN_BARCODEROUTE': 'Barcode based routing is used to route faxes based on the barcode contained in the fax.  Enter the barcode that you want matched to this rule in the Barcode field.  The Alias field is used to describe the purpose for this rule.  For example for a specific service or product.  The Contact field is for an email address, and every fax that arrives for this group will be emailed to the Contact.  The Printer field specifies which CUPS/lpr printer to print the fax on.  Also, you may select a category to automatically categorizing the fax.',
}