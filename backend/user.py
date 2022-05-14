import datetime
from calendar import Calendar
from pydoc import ispackage
from events import Event
from tasks import Task

class User:
    def __init__(self, userID, username, email, password, calendar: Calendar, phoneNumber = None):
        self.userID = userID
        self.username = username
        self.password = password
        self.email = email
        self.calendar = calendar
        self.phoneNumber = phoneNumber
        self.friendsList = {}

    def createEvent(self, startDateTime: datetime.datetime, endDateTime: datetime.datetime,
                    event_name: str, description: str = None, recurring: int = None, isPrivate: bool = True):
        newEvent = Event(startDateTime, endDateTime, event_name, description, recurring, isPrivate)
        self.calendar.addEvent(newEvent)

    def deleteEvent(self, event):
        self.calendar.deleteEvent(event)

    def addTask(self, task: Task):
        self.calendar.addTask(task)

    def addFriend(self, friend):
        self.friendsList[friend.userID] = friend

    def removeFriend(self, friend):
        del self.friendsList[friend.userID] 

    def showFriendList(self):
        for friend in self.friendsList.values():
            #display friend list
            pass

    def showDailyDigest(self, showEvents = True, showTasks = True):
        return self.calendar.dailyDigest(showEvents, showTasks)


