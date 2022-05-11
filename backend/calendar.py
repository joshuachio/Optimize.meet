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
   

#hot
def displayTaskList():
   times = list(taskList.keys())
   times.sort()
   #displaying each task after they are sort chronologically 
   for t in times:
      for task in taskList[t]:
         #display that task
         #We can just return the taskList so it can get called by the frontend? 
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


