import datetime

class Task:
   #Personally think description might have a right to be optional? Up to you here
   def __init__(self, name: str, description: str, dueDate: datetime.datetime, recurring: int = None):
      self.name = name
      self.description = description
      self.dueDate = dueDate
      self.recurring = recurring
      if dueDate in taskList:
         taskList[dueDate].append(self)
      else:
         taskList[dueDate] = [self]