class Survey:
    sid = -1
    gsid = 1
    admin = ""
    adminemail = ""
    anonymized = "N"
    format = "G"
    savetimings = "Y"
    template = "fruity"
    language = ""
    additional_languages = ""
    datestamp = "Y"
    usecookie = "Y"
    allowregister = "N"
    allowsave = "Y"
    autonumber_start = 0
    autoredirect = "N"
    allowprev = "N"
    printanswers = "N"
    ipaddr = "N"
    ipanonymize = "N"
    refurl = "N"
    showsurveypolicynotice = 0
    publicstatistics = "N"
    showdatapolicybutton = 0
    showlegalnoticebutton = 0
    publicgraphs = "N"
    listpublic = "N"
    htmlemail = "Y"
    sendconfirmation = "N"
    tokenanswerspersistence = "Y"
    assessments = "Y"
    usecaptcha = "N"
    usetokens = "N"
    bounce_email = ""
    tokenlength = 15
    showxquestions = "N"
    showgroupinfo = "N"
    shownoanswer = "Y"
    showqnumcode = "X"
    bounceprocessing = "N"
    showwelcome= "Y"
    showprogress = "Y"
    questionindex = 0
    navigationdelay = 0
    nokeyboard = "N"
    alloweditaftercompletion = "N"
    googleanalyticsstyle = 0
    tokeencryptionoptions = ""

    def __init__( self, sid, adminemail, language, admin=None, additional_languages=None ):
        self.sid = sid
        self.adminemail = adminemail
        self.bounce_email = adminemail
        self.language = language
        self.admin = admin
        self.additional_languages = additional_languages

    def __str__( self ):
        attributes = { **self.__class__.__dict__, **vars(self) }
        result = ""
        for attr, value in attributes.items():
            if not attr.startswith("__") and not callable(value):
                result += f"\t\tS\t\t{attr}\t\t{value}\n"
            
        return result