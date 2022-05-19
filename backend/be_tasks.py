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

# class Bug(Task):
#     #a collaborative task/project to work on
#     def __init__(self, name: str, dueDate: datetime.datetime, collaboratorList, description: str = '', recurring: int = None):
#         super().__init__(name, dueDate, description, recurring)
#         self.collaboratorList = collaboratorList

#     def addUser(self, userToAdd: User):
#         self.collaboratorList[userToAdd.userID] = userToAdd

