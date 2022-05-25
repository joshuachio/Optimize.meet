import datetime
import pickle

import jsonpickle
from collections import OrderedDict
from Pyrebase4 import pyrebase
from be_calendar import Calendar
from be_events import Event
from be_tasks import Task
from be_recurring import Recurring
from config_key import config_values


class User:
    def __init__(self, username: str, email: str, password: str, calendar: Calendar, phoneNumber=None):
        # This will create a user in the admin dashboard on firebase (ALSO checks for valid email)
        config = config_values
        firebase = pyrebase.initialize_app(config)
        self.auth = firebase.auth()
        self.db = firebase.database()
        self.storage = firebase.storage()
        userInstance = self.auth.create_user_with_email_and_password(email, password)

        # User Class Attributes
        self.userID = userInstance["localId"]
        self.setUsername(username)
        self.setPassword(password)
        self.email = email
        self.calendar = calendar
        self.phoneNumber = phoneNumber
        self.friendsList = {}

    # Check for valid username (MUST BE 8-30 characters long, only alphanumeric characters)
    def setUsername(self, username):
        if not (7 > len(username) > 30):
            self.username = None
            return
        for char in username:
            if not (48 <= ord(char) <= 57) or not (65 <= ord(char) <= 90) or not (97 <= ord(char) <= 122):
                self.username = None
                return
        self.username = username

    # Check for valid password (Can change the parameters for valid passwords)
    def setPassword(self, password):
        if not (7 > len(password) > 30):
            self.password = None
            return
        for char in password:
            if not (48 <= ord(char) <= 57) or not (65 <= ord(char) <= 90) or not (97 <= ord(char) <= 122):
                self.password = None
                return
        self.password = password

    # Check for valid phone number
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

    # Adds the user to firebase storage
    def addToStorage(self):

        openFile = open('upload.bin', 'wb')
        encodedUser = pickle.dump(self, openFile)
        # encodedUser = encodedUser.decode('utf-8')
        # print(encodedUser, file=openFile)
        openFile.close()
        self.storage.child("users/" + self.userID + ".bin").put('upload.bin')
        # dictOfUser = json.loads(encodedUser)
        # modifiedDictOfUser = OrderedDict(self.modify_dict(dictOfUser))
        # db.child("users").child(self.userID).set(modifiedDictOfUser)

    def modify_dict(self, d):
        new = OrderedDict()
        for k, v in d.items():
            if type(v) == dict:
                v = self.modify_dict(v)
            elif type(v) == list:
                for i in range(len(v)):
                    if type(v[i]) == dict:
                        v[i] = self.modify_dict(v[i])
            if "/" in k:
                temp = k.replace("/", "XX")
                new[temp] = v
            else:
                new[k] = v
        return OrderedDict(new)

    def unmodify_dict(self, d):
        new = {}
        for k, v in d.items():
            if type(v) == dict:
                v = self.unmodify_dict(v)
            elif type(v) == list:
                for i in range(len(v)):
                    if type(v[i]) == dict:
                        v[i] = self.unmodify_dict(v[i])
            if "XX" in k:
                temp = k.replace("XX", "/")
                new[temp] = v
            else:
                new[k] = v
        return OrderedDict(new)


class Session:
    def __init__(self, email, password):
        config = config_values
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        db = firebase.database()
        storage = firebase.storage()
        userInstance = auth.sign_in_with_email_and_password(email, password)
        userID = userInstance['localId']
        storage.child("users/" + userID + ".bin").download('download.bin', 'download.bin')
        openFile = open('download.bin', 'rb')
        self.user = pickle.loads(openFile.read())
        openFile.close()

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
            # display friend list
            pass

    def showAvailability(self, startDatetime, endDatetime, showPrivate: bool = False):
        return self.calendar.showAvailability(startDatetime, endDatetime, showPrivate)

    def showDailyDigest(self, showEvents=True, showTasks=True):
        return self.calendar.dailyDigest(showEvents, showTasks)

    def logOut(self):
        self.user.addToStorage()


#messy testing stuff disregard

cal = Calendar()
cal.taskList == {}
cal.myCal != {}
cal.taskList == {}
cal.myCal[2022] != {}
cal.myCal[2022][1] != {}
cal.myCal[2022][1][1] == []

# Ensures that an event can be added properly.
firstTime = datetime.datetime(2022, 1, 1, 9)
sTime = datetime.datetime(2022, 1, 1, 11)
testEvent = Event(firstTime, sTime, "First Event", "1927 Orrington Avenue", "Video Call")
cal.addEvent(testEvent)
cal.myCal[2022][1][1][0] == testEvent
cal.myCal[2022][1][1][0].description == "Video Call"
cal.displayDay(datetime.datetime(2022, 1, 1)) == [testEvent]
cal.showAvailibility(firstTime, datetime.datetime(2022, 1, 3)) == [testEvent]

secondTime = datetime.datetime(2022, 1, 2, 13)
tTime = datetime.datetime(2022, 1, 2, 15)
recurrance = Recurring("DAILY", 2, datetime.datetime(2022, 2, 1))
secEvent = Event(secondTime, tTime, "Nap Time", "My bed", "Sleeping", recurrance)
cal.addEvent(secEvent)
cal.myCal[2022][1][8][0] == secEvent
cal.myCal[2022][1][2][0] == secEvent
cal.myCal[2022][1][30][0] == secEvent
# print(cal.myCal[2022])

email = "joshuachio10@gmail.com"
password = "JoshuaChio1020"

# u = User("Joshua Chio", email, password, cal, 9725911128)
# u.addToStorage()
f = Session('joshuachio10@gmail.com', 'JoshuaChio1020')
print(f.user.calendar.showAvailibility(firstTime, datetime.datetime(2022, 1, 20)))