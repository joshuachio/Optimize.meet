import user
import be_tasks
import datetime

#This doesn't compile

class Bug(be_tasks.Task):
    #a collaborative task/project to work on
    def __init__(self, name: str, dueDate: datetime.datetime, collaboratorList, description: str = '', recurring: int = None):
        super().__init__(name, dueDate, description, recurring)
        self.collaboratorList = collaboratorList

    def addUser(self, userToAdd: user.User):
        self.collaboratorList[userToAdd.userID] = userToAdd