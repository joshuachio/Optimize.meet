import datetime
from user import User

repeat = {
   1: datetime.timedelta(days=1),
   2: datetime.timedelta(weeks=1)
}

class Task:
   #Personally think description might have a right to be optional? Up to you here
    def __init__(self, name: str, dueDate: datetime.datetime, description: str = '', recurring: int = None):
        self.name = name
        self.description = description
        self.dueDate = dueDate
        self.done = False
        self.recurring = repeat[recurring]

    def finishedTask(self):
        self.done = True

    def unfinishTask(self):
        self.done = False
    
    def setDescription(self, text):
        self.description = text

class Bug(Task):
    #a collaborative task/project to work on
    def __init__(self, name: str, dueDate: datetime.datetime, collaboratorList, description: str = '', recurring: int = None):
        super().__init__(name, dueDate, description, recurring)
        self.collaboratorList = collaboratorList

    def addUser(self, userToAdd: User):
        self.collaboratorList[userToAdd.userID] = userToAdd
