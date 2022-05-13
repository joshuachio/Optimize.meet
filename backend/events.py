import datetime

repeat = {
   1: datetime.timedelta(days=1),
   2: datetime.timedelta(weeks=1)
}


class Event:
   def __init__(self, startDateTime: datetime.datetime, endDateTime: datetime.datetime,
                event_name: str, description: str = None, recurring: int = None, isPrivate: bool = True):
      self.startDateTime = startDateTime
      self.endDateTime = endDateTime
      self.event_name = event_name
      self.description = description
      self.recurring = repeat[recurring]
      self.isprivate = isPrivate
            
   #obv methods
   def setStartDatetime(self, datetime):
      self.startDateTime = datetime

   def setEndDatetime(self, datetime):
      self.endDateTime = datetime

   def setEventName(self, name):
      self.event_name = name

   def setRecurring(self, recurring):
      self.recurring = repeat[recurring]

   def setDescription(self, description):
      self.description = description

class Course(Event):

   def __init__(self, startDateTime: datetime.datetime, endDateTime: datetime.datetime, event_name: str, description: str = None, recurring: int = None, isPrivate: bool = True):
      super().__init__(startDateTime, endDateTime, event_name, description, recurring, isPrivate)

class Meeting(Event):

   def __init__(self, startDateTime: datetime.datetime, endDateTime: datetime.datetime, event_name: str,
                description: str = None, recurring: int = None, isPrivate: bool = True, meetingLink: str = None):
      super().__init__(startDateTime, endDateTime, event_name, description, recurring, isPrivate)
      self.meetingLink = meetingLink

class Personal(Event):

   def __init__(self, startDateTime: datetime.datetime, endDateTime: datetime.datetime, event_name: str, description: str = None, recurring: int = None, isPrivate: bool = True):
      super().__init__(startDateTime, endDateTime, event_name, description, recurring, isPrivate)
