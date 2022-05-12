import datetime
from user import User

class Task:
   #Personally think description might have a right to be optional? Up to you here
   def __init__(self, name: str, dueDate: datetime.datetime, description: str = '', recurring: int = None):
      self.name = name
      self.description = description
      self.dueDate = dueDate
      self.recurring = recurring

class Bug(Task):
    #a collaborative task/project to work on
    def __init__(self, name: str, dueDate: datetime.datetime, collaboratorList, description: str = '', recurring: int = None):
        super().__init__(name, dueDate, description, recurring)
        self.collaboratorList = collaboratorList

    def addUser(self, userToAdd: User):
        self.collaboratorList.append(userToAdd)
