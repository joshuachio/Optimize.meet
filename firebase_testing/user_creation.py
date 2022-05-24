import datetime
import jsonpickle
import json
from collections import OrderedDict
from Pyrebase4 import pyrebase
from be_calendar import Calendar
from be_events import Event
from be_tasks import Task
from be_recurring import Recurring
from config_key import config_values

class User:
    def __init__(self, username: str, email: str, password: str, calendar: Calendar, phoneNumber = None):
        #This will create a user in the admin dashboard on firebase (ALSO checks for valid email)
        config = config_values
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        db = firebase.database()
        storage = firebase.storage()
        userInstance = auth.create_user_with_email_and_password(email, password)

        #User Class Attributes
        self.userID = userInstance["localId"]
        self.setUsername(username)
        self.setPassword(password)
        self.email = email
        self.calendar = calendar
        self.phoneNumber = phoneNumber
        self.friendsList = {}

        #Adds the user to firebase storage
        encodedUser = jsonpickle.encode(self)
        openFile = open('upload.txt', 'w')
        print(encodedUser, file=openFile)
        openFile.close()
        storage.child("users/" + self.userID + ".txt").put('upload.txt')
        # dictOfUser = json.loads(encodedUser)
        # modifiedDictOfUser = OrderedDict(self.modify_dict(dictOfUser))
        # db.child("users").child(self.userID).set(modifiedDictOfUser)

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
        config = {
            "apiKey": "AIzaSyAz5bLpUWAOBouA8Q9_WeloGYDdI1Q9s5g",
            "authDomain": "calendar-be058.firebaseapp.com",
            "databaseURL": "https://calendar-be058-default-rtdb.firebaseio.com",
            "projectId": "calendar-be058",
            "storageBucket": "calendar-be058.appspot.com",
            "messagingSenderId": "765432044481",
            "appId": "1:765432044481:web:7dceaf5af57e8374572d40",
            "measurementId": "G-9Q457P91BV"
        }
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        db = firebase.database()
        storage = firebase.storage()
        userInstance = auth.sign_in_with_email_and_password(email, password)
        userID = userInstance['localID']
        storage.child("users/" + userID + ".txt").download('download.txt', 'download.txt')
        openFile = open('download.txt', 'r')
        self.user = jsonpickle.decode(openFile.read())
        openFile.close()

    def createUser(self, user: User):
        pass


config = {
            "apiKey": "AIzaSyAz5bLpUWAOBouA8Q9_WeloGYDdI1Q9s5g",
            "authDomain": "calendar-be058.firebaseapp.com",
            "databaseURL": "https://calendar-be058-default-rtdb.firebaseio.com",
            "projectId": "calendar-be058",
            "storageBucket": "calendar-be058.appspot.com",
            "messagingSenderId": "765432044481",
            "appId": "1:765432044481:web:7dceaf5af57e8374572d40",
            "measurementId": "G-9Q457P91BV"
        }
firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
# db = firebase.database()
# userInstance = auth.sign_in_with_email_and_password("joshuachio10@gmail.com", "JoshuaChio1020")
# userID = userInstance['localId']
# user = db.child("users").child(userID).get().val()
#
# def unmodify_dict(d):
#     new = {}
#     for k, v in d.items():
#         if type(v) == dict:
#             v = unmodify_dict(v)
#         elif type(v) == list:
#             for i in range(len(v)):
#                 if type(v[i]) == dict:
#                     v[i] = unmodify_dict(v[i])
#         if "XX" in k:
#             temp = k.replace("XX", "/")
#             new[temp] = v
#         else:
#             new[k] = v
#     return new
#
# print(unmodify_dict(user))
# print(jsonpickle.decode(str(user)))






