class Question_Attributes:
    qid = -1
    attribute = ""
    value = ""
    language = ""

    def __init__( self, qid, attribute, value, language=None ):
        self.qid = qid
        self.attribute = attribute
        self.value = value
        self.language = language

    def __str__( self ):
        return "{}\t{}\t{}\t".format( self.qid, self.attribute, self.value ).replace( "None", "" )