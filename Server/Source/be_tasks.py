import datetime


class Task:
    def __init__(self, name: str, dueDate: datetime.datetime, description: str = ''):
        self.name = name
        self.description = description
        self.dueDate = dueDate
        self.done = False

    def finishedTask(self):
        self.done = True

    def unfinishTask(self):
        self.done = False
    
    def setDescription(self, text):
        self.description = text

class Bug(Task):
    #a collaborative task/project to work on
    def __init__(self, name: str, dueDate: datetime.datetime, collaboratorList: list[str] = [], description: str = ''):
        super().__init__(name, dueDate, description)
        self.collaboratorList = collaboratorList

    def addUser(self, email: str):
        self.collaboratorList.append(email)

