import time
# import numpy
#import calendar as cal
import datetime
from be_events import Event
from be_tasks import Task

class Calendar:
   def __init__(self):
      self.myCal = {}
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
         self.myCal[y] = yearDict

   #hot
   def displayTaskList(self, day: datetime.datetime):
      if day.date() in self.taskList:
         return self.taskList[day.date()]
      # times = list(self.taskList.keys())
      # times.sort()
      # #displaying each task after they are sorted chronologically 
      # for t in times:
      #    for task in self.taskList[t]:
      #       #display that task
      #       #We can just return the taskList so it can get called by the frontend? 
      #       pass

   def displayDay(self, day: datetime.datetime, showPrivate: bool = True):
      return self.myCal[day.year][day.month][day]
      # #goes through all the events for that day and displays it one by one
      # for event in eventList:
      #    if showPrivate:
      #       #display event in normal form
      #       pass
      #    else:
      #       if event.isPrivate:
      #          #display event in greyed out form
      #          pass
      #       else:
      #          #display event normally
      #          pass

   def showAvailibility(self, startDay: datetime.datetime, endDay: datetime.datetime, showPrivate: bool = False):
      tdelta = datetime.timedelta(days = 1)
      days = []
      while True:
         days += self.myCal[startDay.year][startDay.month][startDay]
         if startDay == endDay:
            break
         startDay += tdelta
      #returns the a list of events during this time period, but does not display them
      return days

   def addEvent(self, event: Event):
      #Condition for if the event does not recurr
      if event.recurring == None:
         #Adding event to calendar for when the event is on a single day
         if event.startDateTime.date == event.endDateTime.date:
            self.myCal[event.startDateTime.year][event.startDateTime.month][event.startDateTime].append(event)
         #Adding event to calendar if the event is more than one day
         else:
            tdelta = datetime.timedelta(days = 1)
            tempDate = event.startDateTime
            while tempDate.date != event.endDateTime.date:
               self.myCal[tempDate.year][tempDate.month][tempDate].append(event)
               tempDate += tdelta
      #Condition for recurring events
      else:
         self.myCal[event.startDateTime.year][event.startDateTime.month][event.startDateTime].append(event)
         #Daily occurence, the interval represents how many days in between each occurence(one, two, etc days)
         if event.recurring.freq == "DAILY":
            tdelta = datetime.timedelta(days=1) * event.recurring.interval
            tempDate = event.startDateTime
            while tempDate.date != event.recurring.endDate.date:
               self.myCal[tempDate.year][tempDate.month][tempDate].append(event)
               tempDate += tdelta
         #Weekly occurence, the interval represents how many days in between each occurence(one, two, etc weeks)
         elif event.recurring.freq == "WEEKLY":
            tdelta = datetime.timedelta(weeks=1) * event.recurring.interval
            tempDate = event.startDateTime
            #if there is no byDay and the event is just weekly
            if not event.recurring.byDay:
               while tempDate.date != event.recurring.endDate.date:
                  self.myCal[tempDate.year][tempDate.month][tempDate].append(event)
                  tempDate += tdelta
            #byDay represents if the event happens weekly on a certain day of the week
            else:
               tday = datetime.timedelta(days=1)
               #For each day in byDay, this will add the event to that day plus the weekly occurence
               for i in event.recurring.byDay:
                  while tempDate.isoweekday() != i:
                     tempDate += tday
                  while tempDate.date < event.recurring.endDate.date:
                     self.myCal[tempDate.year][tempDate.month][tempDate].append(event)
                     tempDate += tdelta
                  tempDate = event.startDateTime

   #Same method as addEvent, but with remove(event)
   def deleteEvent(self, event: Event):
      #Condition for if the event does not recurr
      if event.recurring == None:
         #Adding event to calendar for when the event is on a single day
         if event.startDateTime.date == event.endDateTime.date:
            self.myCal[event.startDateTime.year][event.startDateTime.month][event.startDateTime].remove(event)
         #Adding event to calendar if the event is more than one day
         else:
            tdelta = datetime.timedelta(days = 1)
            tempDate = event.startDateTime
            while tempDate.date != event.endDateTime.date:
               self.myCal[tempDate.year][tempDate.month][tempDate].remove(event)
               tempDate += tdelta
      #Condition for recurring events
      else:
         self.myCal[event.startDateTime.year][event.startDateTime.month][event.startDateTime].remove(event)
         #Daily occurence, the interval represents how many days in between each occurence(one, two, etc days)
         if event.recurring.freq == "DAILY":
            tdelta = datetime.timedelta(days=1) * event.recurring.interval
            tempDate = event.startDateTime
            while tempDate.date != event.recurring.endDate.date:
               self.myCal[tempDate.year][tempDate.month][tempDate].remove(event)
               tempDate += tdelta
         #Weekly occurence, the interval represents how many days in between each occurence(one, two, etc weeks)
         elif event.recurring.freq == "WEEKLY":
            tdelta = datetime.timedelta(weeks=1) * event.recurring.interval
            tempDate = event.startDateTime
            #if there is no byDay and the event is just weekly
            if not event.recurring.byDay:
               while tempDate.date != event.recurring.endDate.date:
                  self.myCal[tempDate.year][tempDate.month][tempDate].remove(event)
                  tempDate += tdelta
            #byDay represents if the event happens weekly on a certain day of the week
            else:
               tday = datetime.timedelta(days=1)
               #For each day in byDay, this will add the event to that day plus the weekly occurence
               for i in event.recurring.byDay:
                  while tempDate.isoweekday() != i:
                     tempDate += tday
                  while tempDate.date < event.recurring.endDate.date:
                     self.myCal[tempDate.year][tempDate.month][tempDate].remove(event)
                     tempDate += tdelta
                  tempDate = event.startDateTime

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
      events = self.myCal[today.year][today.month][today]
      tasks = self.taskList[today.date]
      if not showEvents:
         return tasks
      elif not showTasks:
         return events
      allTODO = events + tasks
      return allTODO
