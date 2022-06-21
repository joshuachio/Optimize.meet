import time
# import numpy
#import calendar as cal
import datetime
from be_events import Event
from be_tasks import Task, Bug
from be_recurring import Recurring

class Calendar:
   def __init__(self):
      self.myCal = {}
      self.taskList = {}
      yearr = datetime.datetime.today().year
      for y in range(yearr, yearr+5):
         yearDict = {}
         for month in range(1, 13):
            monthDict = {}
            #April, June, September, November have 30 Days
            if month == 4 or month == 6 or month == 9 or month == 11:
                  monthDict = {}
                  for d in range(30):
                     monthDict[d+1] = []
               #Feburary has 28 or 29 days
            elif month == 2:
                  if y % 4 == 0:
                     for d in range(29):
                        monthDict[d+1] = []
               #Not a leap year case
                  else:
                     for d in range(28):
                        monthDict[d+1] = []
            #All other months have 31 days
            else:
                  for d in range(31):
                     monthDict[d+1] = []
            yearDict[month] = monthDict
         self.myCal[y] = yearDict

   def update(self, date: datetime.datetime = datetime.datetime.today()):
      #Called on everything, pretty much ensures there is a 5 year horizon on anything we enter just to validate. 
      curyear = date.year
      if curyear in self.myCal.keys():
         return 
      else:
         furthestyear = max(self.myCal.keys())
         for y in range(furthestyear+1, curyear+5):
            yearDict = {}
            for month in range(1, 13):
               monthDict = {}
               #April, June, September, November have 30 Days
               if month == 4 or month == 6 or month == 9 or month == 11:
                  monthDict = {}
                  for d in range(30):
                     monthDict[d+1] = []
               #Feburary has 28 or 29 days
               elif month == 2:
                  if y % 4 == 0:
                     for d in range(29):
                        monthDict[d+1] = []
               #Not a leap year case
                  else:
                     for d in range(28):
                        monthDict[d+1] = []
               #All other months have 31 days
               else:
                  for d in range(31):
                     monthDict[d+1] = []
               yearDict[month] = monthDict
            self.myCal[y] = yearDict
      pass


   def addEvent(self, event: Event):
      #Condition for if the event does not recurr
      if event.recurring == None:
         #Adding event to calendar for when the event is on a single day
         if event.startDateTime.date is event.endDateTime.date:
            self.myCal[event.startDateTime.year][event.startDateTime.month][event.startDateTime.day].append(event)
         #Adding event to calendar if the event is more than one day
         else:
            tdelta = datetime.timedelta(days = 1)
            tempDate = event.startDateTime
            while tempDate <= event.endDateTime:
               self.myCal[tempDate.year][tempDate.month][tempDate.day].append(event)
               tempDate += tdelta
      #Condition for recurring events
      else:
         # self.myCal[event.startDateTime.year][event.startDateTime.month][event.startDateTime.day].append(event)
         #Daily occurence, the interval represents how many days in between each occurence(one, two, etc days)
         if event.recurring.freq == "DAILY":
            tdelta = datetime.timedelta(days=1) * event.recurring.interval
            tempDate = event.startDateTime
            while tempDate <= event.recurring.endDate:
               self.myCal[tempDate.year][tempDate.month][tempDate.day].append(event)
               tempDate += tdelta
         #Weekly occurence, the interval represents how many days in between each occurence(one, two, etc weeks)
         elif event.recurring.freq == "WEEKLY":
            tdelta = datetime.timedelta(weeks=1) * event.recurring.interval
            tempDate = event.startDateTime
            #if there is no byDay and the event is just weekly
            if not event.recurring.byDay:
               while tempDate <= event.recurring.endDate:
                  self.myCal[tempDate.year][tempDate.month][tempDate.day].append(event)
                  tempDate += tdelta
            #byDay represents if the event happens weekly on a certain day of the week
            else:
               tday = datetime.timedelta(days=1)
               #For each day in byDay, this will add the event to that day plus the weekly occurence
               for i in event.recurring.byDay:
                  while tempDate.isoweekday() != i:
                     tempDate += tday
                  while tempDate <= event.recurring.endDate:
                     self.myCal[tempDate.year][tempDate.month][tempDate.day].append(event)
                     tempDate += tdelta
                  tempDate = event.startDateTime

   #Same method as addEvent, but with remove(event)
   def deleteEvent(self, event: Event):
      #Condition for if the event does not recurr
      if event.recurring == None:
         #Adding event to calendar for when the event is on a single day
         if event.startDateTime.date == event.endDateTime.date:
            self.myCal[event.startDateTime.year][event.startDateTime.month][event.startDateTime.day].remove(event)
         #Adding event to calendar if the event is more than one day
         else:
            tdelta = datetime.timedelta(days = 1)
            tempDate = event.startDateTime
            while tempDate <= event.endDateTime:
               # if event in self.myCal[tempDate.year][tempDate.month][tempDate.day]:
               self.myCal[tempDate.year][tempDate.month][tempDate.day].remove(event)
               tempDate += tdelta
      #Condition for recurring events
      else:
         # self.myCal[event.startDateTime.year][event.startDateTime.month][event.startDateTime.day].remove(event)
         #Daily occurence, the interval represents how many days in between each occurence(one, two, etc days)
         if event.recurring.freq == "DAILY":
            tdelta = datetime.timedelta(days=1) * event.recurring.interval
            tempDate = event.startDateTime
            while tempDate <= event.recurring.endDate:
               self.myCal[tempDate.year][tempDate.month][tempDate.day].remove(event)
               tempDate += tdelta
         #Weekly occurence, the interval represents how many days in between each occurence(one, two, etc weeks)
         elif event.recurring.freq == "WEEKLY":
            tdelta = datetime.timedelta(weeks=1) * event.recurring.interval
            tempDate = event.startDateTime
            #if there is no byDay and the event is just weekly
            if not event.recurring.byDay:
               while tempDate <= event.recurring.endDate:
                  self.myCal[tempDate.year][tempDate.month][tempDate.day].remove(event)
                  tempDate += tdelta
            #byDay represents if the event happens weekly on a certain day of the week
            else:
               tday = datetime.timedelta(days=1)
               #For each day in byDay, this will add the event to that day plus the weekly occurence
               for i in event.recurring.byDay:
                  while tempDate.isoweekday() != i:
                     tempDate += tday
                  while tempDate <= event.recurring.endDate:
                     self.myCal[tempDate.year][tempDate.month][tempDate.day].remove(event)
                     tempDate += tdelta
                  tempDate = event.startDateTime


   def displayDay(self, day: datetime.datetime, showPrivate: bool = True):
      return self.myCal[day.year][day.month][day.day]
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
      eventList = []
      tempDate = startDay
      while tempDate <= endDay:
         eventList += self.myCal[tempDate.year][tempDate.month][tempDate.day]
         tempDate += tdelta
      return eventList

   #adds task to the task dictionary 
   def addTask(self, task: Task):
      if task.dueDate.date in self.taskList:
        self.taskList[task.dueDate.date].append(task)
      else:
        self.taskList[task.dueDate.date] = [task]

   def removeTask(self, task: Task):
      if task.dueDate.date in self.taskList:
        self.taskList[task.dueDate.date].remove(task)


   #display the list of tasks for that day
   def displayTaskList(self, day: datetime.datetime):
      if day.date in self.taskList:
         return self.taskList[day.date]
      return []
      # times = list(self.taskList.keys())
      # times.sort()
      # #displaying each task after they are sorted chronologically 
      # for t in times:
      #    for task in self.taskList[t]:
      #       #display that task
      #       #We can just return the taskList so it can get called by the frontend? 
      #       pass

   def dailyDigest(self, today: datetime.date, showEvents = True, showTasks = True):
      # today = datetime.date(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)
      if today.date not in self.taskList:
         tasks = []
      else:
         tasks = self.taskList[today.date]
      events = self.myCal[today.year][today.month][today.day]
      if not showEvents or not self.taskList:
         return tasks
      elif not showTasks or not self.taskList:
         return events
      allTODO = events + tasks
      return allTODO