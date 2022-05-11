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
      #Adding event to calendar for when the event is on a single day
      if startDateTime.date == endDateTime.date:
         calendar[startDateTime.year][startDateTime.month][startDateTime].append(self)
      #Adding event to calendar if the event is more than one day
      else:
         tdelta = datetime.timedelta(days = 1)
         while True:
            calendar[startDateTime.year][startDateTime.month][startDateTime].append(self)
            if startDateTime.date == endDateTime.date:
               break
            startDateTime += tdelta
            
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

   def __init__(self, startDateTime: datetime.datetime, endDateTime: datetime.datetime, event_name: str, description: str = None, recurring: int = None, isPrivate: bool = True):
      super().__init__(startDateTime, endDateTime, event_name, description, recurring, isPrivate)
   #Doesn't course need to take in academic calendar or are we interpreting that seperately?

class Personal(Event):

   def __init__(self, startDateTime: datetime.datetime, endDateTime: datetime.datetime, event_name: str, description: str = None, recurring: int = None, isPrivate: bool = True):
      super().__init__(startDateTime, endDateTime, event_name, description, recurring, isPrivate)
