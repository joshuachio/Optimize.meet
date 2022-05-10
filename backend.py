import time
# import numpy
import calendar as cal
import datetime

calendar = {}

for y in range(2022, 2026):
    yearDict = {}
    for month in range(1, 13):
        monthDict = {}
        if month == 4 or month == 6 or month == 9 or month == 11:
            monthDict = {}
            for d in range(1, 31):
                date = datetime.datetime(y, month, d)
                monthDict[date] = []
        elif month == 2:
            if y % 4 == 0:
                for d in range(1, 30):
                    date = datetime.datetime(y, month, d)
                    monthDict[date] = []
            else:
                for d in range(1, 29):
                    date = datetime.datetime(y, month, d)
                    monthDict[date] = []
        else:
            for d in range(1, 32):
                date = datetime.datetime(y, month, d)
                monthDict[date] = []
        yearDict[month] = monthDict
    calendar[y] = yearDict

taskList = {}

# days = {
#    0:'Monday',
#    1:'Tuesday',
#    2:'Wednesday',
#    3:'Thursday',
#    4:'Friday',
#    5:'Saturday',
#    6:'Sunday'
# }
   
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
      if startDateTime.date == endDateTime.date:
         calendar[startDateTime.year][startDateTime.month][startDateTime].append(self)
      else:
         tdelta = datetime.timedelta(days = 1)
         while True:
            calendar[startDateTime.year][startDateTime.month][startDateTime].append(self)
            if startDateTime.date == endDateTime.date:
               break
            startDateTime += tdelta
            

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

   def __init__(self, startDateTime: datetime.datetime, endDateTime: datetime.datetime, event_name: str, description: str, recurring: int):
       super().__init__(startDateTime, endDateTime, event_name, description, recurring)

class Meeting(Event):

   def __init__(self, startDateTime: datetime.datetime, endDateTime: datetime.datetime, event_name: str, description: str, recurring: int):
       super().__init__(startDateTime, endDateTime, event_name, description, recurring)

class Personal(Event):

   def __init__(self, startDateTime: datetime.datetime, endDateTime: datetime.datetime, event_name: str, description: str, recurring: int):
      super().__init__(startDateTime, endDateTime, event_name, description, recurring)

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
   for t in times:
      for task in taskList[t]:
         #display that task
         pass


def displayDay(day: datetime.datetime, showPrivate: bool = True):
   eventList = calendar[day.year][day.month][day]
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
   while True:
      displayDay(startDay, showPrivate)
      if startDay == endDay:
         break
      startDay += tdelta


# class Day:
   
#    def __init__(self, day: datetime.date, dayofweek):
#        self.day = day
#        self.dayofweek = days[dayofweek]
#        self.eventList = {}
   
#    def dayofweek(self):
#       return self.dayofweek
   
#    def addToEventList(self, addEvent: Event):
#       if (addEvent.start_date is self.day):
#          self.eventList[addEvent.start_time] = (addEvent)

#    def displayEvents(self):
#       keyOrder = list(self.eventList.keys())
#       keyOrder.sort()
#       for time in keyOrder:
#          self.display(time, self.eventList[time].event_name)
   
#    def display(self, time: datetime.time, eventName):
#       ##some frontend for displaying stuff
#       None


# class Month:
#    def __init__(self, month, year):     
#       self.month = month #an integer (1-12) representing the month
#       self.daysList = [None]
#       if month == 4 or month == 6 or month == 9 or month == 11:
#          pass
#       elif month == 28 or month == 29:
#          pass
#       else:
#          for i in range(1, 32):
#             tempDate = datetime.date(year, month, i)
#             temp = Day(tempDate, )
#             self.daysList.append(temp)



#    def addDays(self, day: Day):
#       self.daysList[day.day.day] = day #just maps the day (1-31) to that Day object

#    def display(self):
#       #display the month visually
#       pass

# class Year:
#    def __init__(self, year):
#       self.year = year
#       self.monthsList = [None]
#       for i in range(1, 13):
#          temp = Month(i, year)
#          self.monthsList.append(temp)

#    def display(self):
#       #display the year visually
#       pass

   

