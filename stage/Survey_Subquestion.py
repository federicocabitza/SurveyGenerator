from StringRepresentation import StringRepresentation

class Survey_Subquestion:

    qid = -1
    parent_qid = -1
    sid = -1
    gid = -1
    _class = "SQ"
    _type = ""
    title = ""
    question = ""
    help = ""
    other = ""
    question_order = ""
    language = ""
    scale_id = -1
    same_default = ""
    relevance = ""
    modulename = ""
    _encrypted = "N"
    question_theme_name = ""
    same_script = ""

    def __init__(self, qid, parent_qid, sid, gid, _type,
        title, other, question_order, scale_id, same_default,
        relevance, modulename=None, _encrypted=None, question=None,
        language=None, help=None, question_theme_name=None, same_script=None):

            self.qid = qid
            self.parent_qid = parent_qid
            self.sid = sid
            self.gid = gid
            self._class = "SQ"
            self._type = _type
            self.title = title
            self.question = question
            self.help = help
            self.other = other
            self.question_order = question_order
            self.language = language
            self.scale_id = scale_id
            self.same_default = same_default
            self.relevance = relevance
            self.modulename = modulename
            self._encrypted = _encrypted
            self.question_theme_name = question_theme_name
            self.same_script = same_script

    def __str__(self):
        return str( StringRepresentation(self) )

    def __or__(self, other):
        if not isinstance( other, Survey_Subquestion ):
            return NotImplemented

        combined_attributes = {
            "_class": self._class or other._class,
            "qid": self.qid or other.qid,
            "parent_qid": self.parent_qid or other.parent_qid,
            "sid": self.sid or other.sid,
            "gid": self.gid or other.gid,
            "_type": self._type or other._type,
            "title": self.title or other.title,
            "question": self.question or other.question,
            "help": self.help or other.help,
            "other": self.other or other.other,
            "question_order": self.question_order or other.question_order,
            "language": self.language or other.language,
            "scale_id": self.scale_id or other.scale_id,
            "same_default": self.same_default or other.same_default,
            "relevance": self.relevance or other.relevance,
            "modulename": self.modulename or other.modulename,
            "_encrypted": self._encrypted or other._encrypted,
            "question_theme_name": self.question_theme_name or other.question_theme_name,
            "same_script": self.same_script or other.same_script,
            "script": self.script or other.script
        }
        return Survey_Subquestion( **combined_attributes )