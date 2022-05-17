import datetime
from calendar import Calendar
from pydoc import ispackage
from re import U
from tkinter import E
from be_events import Event
from be_tasks import Task

class User:
    def __init__(self, userID, username: str, email: str, password: str, calendar: Calendar, phoneNumber = None):
        self.userID = userID
        self.setUsername(username)
        self.setPassword(password)
        self.setEmail(email)
        self.calendar = calendar
        self.setPhoneNumber(phoneNumber)
        self.friendsList = {}

    #Check for valid username (MUST BE 8-30 characters long, only alphanumeric characters)
    def setUsername(self, username):
        if not (7 > len(username) > 30):
            self.username = None
            return
        for char in username:
            if not (48 <= ord(char) <= 57) or not (65 <= ord(char) <= 90) or not (97 <= ord(char) <= 122):
                self.username = None
                return
        self.username = username

    #Check for valid password (Can change the parameters for valid passwords)
    def setPassword(self, password):
        if not (7 > len(password) > 30):
            self.password = None
            return
        for char in password:
            if not (48 <= ord(char) <= 57) or not (65 <= ord(char) <= 90) or not (97 <= ord(char) <= 122):
                self.password = None
                return
        self.password = password

    #Checks valid email
    def setEmail(self, email):
        try:
            check = email.split("@")
            if "." in check[1]:
                self.email = email
            else:
                self.email = None
        except:
            self.email = None

    #Check for valid phone number
    def setPhoneNumber(self, number):
        if number.isdigit():
            self.phoneNumber = number
            return
        count = 0
        if "+" in number:
            for char in number:
                if char.isdigit():
                    count += 1
            if count == 11:
                self.phoneNumber = number
                return
        else:
            for char in number:
                if char.isdigit():
                    count += 1
            if count == 10:
                self.phoneNumber = number

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

    def showAvailability(self, startDatetime, endDatetime, showPrivate: bool = False):
        return self.calendar.showAvailability(startDatetime, endDatetime, showPrivate)

    def showDailyDigest(self, showEvents = True, showTasks = True):
        return self.calendar.dailyDigest(showEvents, showTasks)


