import time
# import numpy
#import calendar as cal
import datetime
from events import Event
from tasks import Task

class Calendar:
   def __init__(self):
      self.calendar = {}
      self.taskList = {}
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
         self.calendar[y] = yearDict

   #hot
   def displayTaskList(self):
      times = list(self.taskList.keys())
      times.sort()
      #displaying each task after they are sorted chronologically 
      for t in times:
         for task in self.taskList[t]:
            #display that task
            #We can just return the taskList so it can get called by the frontend? 
            pass

   def displayDay(self, day: datetime.datetime, showPrivate: bool = True):
      eventList = self.calendar[day.year][day.month][day]
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

   def showAvailibility(self, startDay: datetime.datetime, endDay: datetime.datetime, showPrivate: bool = False):
      tdelta = datetime.timedelta(days = 1)
      days = []
      while True:
         days += self.calendar[startDay.year][startDay.month][startDay]
         if startDay == endDay:
            break
         startDay += tdelta
      #returns the a list of events during this time period, but does not display them
      return days

   def addEvent(self, event: Event):
      #Adding event to calendar for when the event is on a single day
      if event.startDateTime.date == event.endDateTime.date:
         self.calendar[event.startDateTime.year][event.startDateTime.month][event.startDateTime].append(event)
      #Adding event to calendar if the event is more than one day
      else:
         tdelta = datetime.timedelta(days = 1)
         tempStartDate = event.startDateTime
         while True:
            self.calendar[tempStartDate.year][tempStartDate.month][tempStartDate].append(event)
            if tempStartDate.date == tempStartDate.date:
               break
            tempStartDate += tdelta

   def deleteEvent(self, event: Event):
      #Same as adding event, but with remove() function
      if event.startDateTime.date == event.endDateTime.date:
         self.calendar[event.startDateTime.year][event.startDateTime.month][event.startDateTime].remove(event)
      #Removing event to calendar if the event is more than one day
      else:
         tdelta = datetime.timedelta(days = 1)
         tempStartDate = event.startDateTime
         while True:
            self.calendar[tempStartDate.year][tempStartDate.month][tempStartDate].remove(event)
            if tempStartDate.date == tempStartDate.date:
               break
            tempStartDate += tdelta

   #adds task to the task dictionary 
   def addTask(self, task: Task):
      if task.dueDate.date in self.taskList:
        self.taskList[task.dueDate.date].append(task)
      else:
        self.taskList[task.dueDate.date] = [task]

   def removeTask(self, task: Task):
      if task.dueDate.date in self.taskList:
        self.taskList[task.dueDate.date].remove(task)

   def dailyDigest(self, showEvents = True, showTasks = True):
      today = datetime.datetime.today()
      events = self.calendar[today.year][today.month][today]
      tasks = self.taskList[today.date]
      if not showEvents:
         return tasks
      elif not showTasks:
         return events
      allTODO = events + tasks
      return allTODO


