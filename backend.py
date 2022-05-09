from msilib.schema import ReserveCost
import time

from django.conf import ENVIRONMENT_VARIABLE
import numpy
import calendar
import datetime




class Recurring:

   def __init__(self, type):
      if type == 0:
         self.reccurance = "DAILY"
      elif type == 1:
         self.reccurance = "WEEKLY"

class Event:
   
   def __init__(self, start_time: datetime.time, end_time: datetime.time, start_date: datetime.date,
                 end_date: datetime.date, event_name: str, recurring: Recurring, description: str):
      self.start_time = start_time
      self.end_time = end_time
      self.start_date = start_date
      self.end_date = end_date
      self.event_name = event_name
      self.recurring = recurring #needs to be a "recurring type" with weekly/daily/etc
      self.description = description

   def setStartTime(self, time):
      self.start_time = time

   def setEndTime(self, time):
      self.end_time = time

   def setStartDate(self, date):
      self.start_date = date

   def setEndDate(self, date):
      self.end_date = date

   def setEventName(self, name):
      self.event_name = name

   def setRecurring(self, recurring: Recurring):
      self.recurring = recurring

   def setDescription(self, description):
      self.description = description

   


class Course(Event):

   def __init__(self, start_time: datetime.time, end_time: datetime.time, start_date: datetime.date,
                 end_date: datetime.date, event_name: str, recurring: Recurring, description: str):
      super().__init__(start_time, end_time, start_date, end_date, event_name, recurring, description)
      self.

class Meeting(Event):

   def __init__(self, start_time: datetime.time, end_time: datetime.time, start_date: datetime.date,
                 end_date: datetime.date, event_name: str, recurring: Recurring, description: str):
      super().__init__(start_time, end_time, start_date, end_date, event_name, recurring, description)
      self.


class Personal(Event):

   def __init__(self, start_time: datetime.time, end_time: datetime.time, start_date: datetime.date,
               end_date: datetime.date, event_name: str, recurring: Recurring, description: str):
      super().__init__(start_time, end_time, start_date, end_date, event_name, recurring, description)


class Day:
   
   def __init__(self,day: datetime.date):
       self.day = day
       self.eventList = {}

   def addToEventList(self, addEvent: Event):
      if (addEvent.start_date is self.day):
         self.eventList[addEvent.start_time] = (addEvent)

   def displayEvents(self):
      keyOrder = list(self.eventList.keys())
      keyOrder.sort()
      for time in keyOrder:
         self.display(self.eventList[time].event_name)
   
   def display(self):
      ##some frontend for displaying stuff
      None

   

