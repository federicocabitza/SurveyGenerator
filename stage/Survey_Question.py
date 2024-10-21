from StringRepresentation import StringRepresentation
import re

class Survey_Question:

    _id = -1
    qid = -1
    parent_qid = -1
    sid = -1
    gid = -1
    _class = "Q"
    _type = ""
    title = ""
    question = ""
    help = ""
    other = ""
    question_order = ""
    language = ""
    scale_id = 0
    same_default = ""
    relevance = ""
    modulename = ""
    _encrypted = "N"
    _class = "Q"
    validation = ""
    mandatory = "N"
    question_theme_name = ""
    same_script = ""
    script = ""
    preg =""

    #Attributes
    public_statistics = ""
    scale_export = ""
    answer_order = ""
    exclude_all_others = ""
    min_answers = ""
    max_answers = ""
    random_order = ""
    repeat_headings = ""
    use_dropdown = ""
    answer_width = ""
    time_limit_warning_style = ""
    time_limit_warning_message = ""
    time_limit_warning_display_time = ""
    time_limit_warning_2_style = ""
    time_limit_warning_2_message = ""
    time_limit_warning_2_display_time = ""
    time_limit_warning_2 = ""
    time_limit_warning = ""
    time_limit_timer_style = ""
    time_limit_message_style = ""
    time_limit_message_delay = ""
    time_limit_message = ""
    time_limit_disable_prev = ""
    time_limit_disable_next = ""
    time_limit_countdown_message = ""
    time_limit_action = ""
    time_limit = ""
    statistics_showgraph = ""
    statistics_graphtype = ""
    save_as_default = ""
    random_group = ""
    page_break = ""
    hide_tip = ""
    hidden = ""
    cssclass = ""
    array_filter = ""
    array_filter_exclude = ""
    array_filter_style = ""
    display_columns = ""
    em_validation_q = ""
    em_validation_q_tip = ""
    other_comment_mandatory = ""
    other_numbers_only = ""
    other_position = ""
    other_position_code = ""
    other_replace_text = ""
    printable_help = ""


    def __init__(self, qid, question=None, validation=None,
        help=None, language=None, _encrypted=None,
        question_theme_name=None, same_script=None,
        script=None, parent_qid=None, sid=None, gid=None,
        title=None, other=None, mandatory=None,
        question_order=None, scale_id=None, same_default=None,
        _id=None, _type=None, relevance=None, modulename=None,
        preg=None, _class=None):
            self._id = _id
            self._class = "Q"
            self.qid = qid
            self.parent_qid = parent_qid
            self.sid = sid
            self.gid = gid
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
            self._encrypted = "N"
            self.validation = validation
            self.mandatory = mandatory
            self.question_theme_name = question_theme_name
            self.same_script = same_script
            self.script = script
            self.preg = preg


    def __or__(self, other):
        if not isinstance( other, Survey_Question ):
            return NotImplemented

        combined_attributes = {
            "_id": self._id or other._id,
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
            "validation": self.validation or other.validation,
            "mandatory": self.mandatory or other.mandatory,
            "question_theme_name": self.question_theme_name or other.question_theme_name,
            "same_script": self.same_script or other.same_script,
            "script": self.script or other.script,
            "preg": self.preg or other.preg,
        }
        return Survey_Question( **combined_attributes )

    def intersect(list1, list2, key):
        # Find the intersection of the two lists based on the `qid` attribute
        return [item1 for item1 in list1 for item2 in list2 if getattr(item1, key) == (item2, key)]

    def setTitle( self, i ):
        if isinstance( self.title, str ) and self.title:
            match = re.findall(r'\d+', self.title)

            if match:
                number = int(match[0])
                new_number = number + i
                new_string = re.sub(r'\d+', str(new_number), self.title)
                return new_string
            else:
                return self.title




    def __str__(self):
        return str( StringRepresentation(self) )