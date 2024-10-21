class Answer:
   _id = -1
   aid = -1
   qid = -1
   _class = "A"
   code = 0
   answer = ""
   sortorder = 0
   assessment_value = 0
   language = ""
   scale_id = 0

   def __init__(self, qid=None, scale_id=None, code=None, sortorder=None, assessment_value=None,
      language=None, answer=None, aid=None, _id=None, _class=None):
         self._class = "A"
         self.aid = aid
         self.qid = qid
         self.code = code
         self.answer = answer
         self.sortorder = sortorder
         self.assessment_value = assessment_value
         self.language = language
         self._id = _id
         self.scale_id = scale_id

   @staticmethod
   def from_list( attributes ):
      if len(attributes) != 7:
         raise ValueError( "Expected a list with exactly 8 elements." )
      return Answer(*attributes)

   def __str__(self):
      return """{}\t\t{}\t{}\t{}\t\t{}\t\t{}\t\t\t\t\t\t\t\t\t\t\t\t\t\t{}""".format(self.qid, self._class,
       self.scale_id, self.code, self.answer, self.language, self.assessment_value).replace("None", "")

   def __or__(self, other):
      if not isinstance( other, Answer ):
         return NotImplemented

      combined_attributes = {
         "_id": self._id or other._id,
         "_class": self._class or other._class,
         "aid": self.aid or other.aid,
         "qid": self.qid or other.qid,
         "code": self.code or other.code,
         "answer": self.answer or other.answer,
         "sortorder": self.sortorder or other.sortorder,
         "assessment_value": self.assessment_value or other.assessment_value,
         "language": self.language or other.language,
         "scale_id": self.scale_id or other.scale_id,
      }
      return Answer( **combined_attributes )