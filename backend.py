import time
# import numpy
import calendar as cal
import datetime

calendar = {}

#I can verify that this works but we should probably make calendar a class so we can give it methods?
for y in range(2022, 2026):
    yearDict = {}
    for month in range(1, 13):
        monthDict = {}
        #April, June, September, November have 30 Days
        if month == 4 or month == 6 or month == 9 or month == 11:
            monthDict = {}
            for d in range(1, 31):
                date = datetime.datetime(y, month, d)
                monthDict[date] = []
                
         #Feburary has 28 or 29 days
        elif month == 2:
            if y % 4 == 0:
                for d in range(1, 30):
                    date = datetime.datetime(y, month, d)
                    monthDict[date] = []
         #Not a leap year case
            else:
                for d in range(1, 29):
                    date = datetime.datetime(y, month, d)
                    monthDict[date] = []
        #All other months have 31 days
        else:
            for d in range(1, 32):
                date = datetime.datetime(y, month, d)
                monthDict[date] = []
        yearDict[month] = monthDict
    calendar[y] = yearDict


taskList = {}
   
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

class Personal(Event):

   def __init__(self, startDateTime: datetime.datetime, endDateTime: datetime.datetime, event_name: str, description: str = None, recurring: int = None, isPrivate: bool = True):
      super().__init__(startDateTime, endDateTime, event_name, description, recurring, isPrivate)

class Task:
   
   def __init__(self, name: str, description: str, dueDate: datetime.datetime, recurring: int = None):
      self.name = name
      self.description = description
      self.dueDate = dueDate
      self.recurring = recurring
      if dueDate in taskList:
         taskList[dueDate].append(self)
      else:
         taskList[dueDate] = [self]

def displayTaskList():
   times = list(taskList.keys())
   times.sort()
   #displaying each task after they are sort chronologically 
   for t in times:
      for task in taskList[t]:
         #display that task
         pass


def displayDay(day: datetime.datetime, showPrivate: bool = True):
   eventList = calendar[day.year][day.month][day]
   #goes through all the events for that day and displays it one by one
   for event in eventList:
      if showPrivate:
         #display event in normal form
         pass
      else:
         if event.isPrivate:
            #display event in greyed out form
            pass
         else:
            #display event normally
            pass


def showAvailibility(startDay: datetime.datetime, endDay: datetime.datetime, showPrivate: bool = False):
   tdelta = datetime.timedelta(days = 1)
   #goes day by day to display all the events
   while True:
      displayDay(startDay, showPrivate)
      if startDay == endDay:
         break
      startDay += tdelta


