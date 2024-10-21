from StringRepresentation import StringRepresentation

class Group:
   _id = -1
   gid = -1
   sid = -1
   _class = "G"
   group_name = ""
   group_order = ""
   description = ""
   language = ""
   randomization_group = ""
   grelevance = ""

   def __init__( self, gid, group_order, randomization_group, grelevance, sid=None,
      _id=None, group_name=None, description=None, language=None ):
         self._class = "G"
         self._id = _id
         self.gid = gid
         self.sid = sid
         self.group_name = group_name
         self.group_order = group_order
         self.description = description
         self.language = language
         self.randomization_group = randomization_group
         self.grelevance = grelevance

   def __str__( self ):
      return str( StringRepresentation(self) )

   def __or__(self, other):
      if not isinstance( other, Group ):
         return NotImplemented

      combined_attributes = {
         "gid": self.gid or other.gid,
         "group_order": self.group_order or other.group_order,
         "randomization_group": self.randomization_group or other.randomization_group,
         "grelevance": self.grelevance or other.grelevance,
         "sid": self.sid or other.sid,
         "_id": self._id or other._id,
         "group_name": self.group_name or other.group_name,
         "description": self.description or other.description,
         "language": self.language or other.language
      }
      return Group( **combined_attributes )