import datetime
import pickle
import sys
sys.path.append('../Calendar')
import collections
import jsonpickle
from collections import OrderedDict
import pyrebase
from .be_calendar import Calendar
try:
    from .config_key import config_values
except:
    pass


class User:
    def __init__(self, username: str, email: str, password: str, calendar: Calendar, phoneNumber: int=None):
        # User Class Attributes
        self.setUsername(username)
        self.setPassword(password)
        self.email = email
        self.calendar = calendar
        self.phoneNumber = phoneNumber
        self.friendsList = {}

        #This section initializes the connection to firebase
        config = config_values
        firebase = pyrebase.initialize_app(config)
        self.auth = firebase.auth()
        self.db = firebase.database()
        self.storage = firebase.storage()

        # This will create a user in the admin dashboard on firebase (ALSO checks for valid email)
        self.userInstance = self.auth.create_user_with_email_and_password(email, password)
        self.userID = self.userInstance["localId"]
        self.addToStorage()

    # Check for valid username (MUST BE 8-30 characters long, only alphanumeric characters)
    def setUsername(self, username):
        if not (7 <= len(username) <= 30):
            raise(InvalidUsername)
        for char in username:
            if not char.isalnum():
                raise(InvalidUsername)
        self.username = username

    # Check for valid password (Can change the parameters for valid passwords)
    def setPassword(self, password):
        if not (7 <= len(password) <= 30):
            raise(InvalidPassword)
        for char in password:
            if not char.isalnum():
                raise(InvalidPassword)
        self.password = password

    # Check for valid phone number
    def setPhoneNumber(self, number):
        count = 0
        for char in str(number):
            if char.isdigit():
                count += 1
        if count != 10:
            raise(InvalidPhoneNumber)
        self.phoneNumber = int(number)

    # Adds the user to firebase storage in bytes format
    def addToStorage(self):
        openFile = open('upload.bin', 'wb')
        pickle.dump(self, openFile)
        openFile.close()
        self.storage.child("users/" + self.userID + ".bin").put('upload.bin')

    def forgotPassword(self):
        self.auth.send_password_reset_email(self.email)

    def deleteAccount(self):
        self.auth.delete_user_account(self.userInstance['idToken'])

    # def modify_dict(self, d):
    #     new = OrderedDict()
    #     for k, v in d.items():
    #         if type(v) == dict:
    #             v = self.modify_dict(v)
    #         elif type(v) == list:
    #             for i in range(len(v)):
    #                 if type(v[i]) == dict:
    #                     v[i] = self.modify_dict(v[i])
    #         if "/" in k:
    #             temp = k.replace("/", "XX")
    #             new[temp] = v
    #         else:
    #             new[k] = v
    #     return OrderedDict(new)
    #
    # def unmodify_dict(self, d):
    #     new = {}
    #     for k, v in d.items():
    #         if type(v) == dict:
    #             v = self.unmodify_dict(v)
    #         elif type(v) == list:
    #             for i in range(len(v)):
    #                 if type(v[i]) == dict:
    #                     v[i] = self.unmodify_dict(v[i])
    #         if "XX" in k:
    #             temp = k.replace("XX", "/")
    #             new[temp] = v
    #         else:
    #             new[k] = v
    #     return OrderedDict(new)


class Session:
    def __init__(self, email, password):
        #Initialize firebase connection
        config = config_values
        firebase = pyrebase.initialize_app(config)
        self.auth = firebase.auth()
        storage = firebase.storage()

        # Log in for the user using email and password
        try:
            userInstance = self.auth.sign_in_with_email_and_password(email, password)
            userID = userInstance['localId']
            storage.child("users/" + userID + ".bin").download('download.bin', 'download.bin')
            openFile = open('download.bin', 'rb')
            # self.user is the User instance corresponding to the login info
            self.user = pickle.loads(openFile.read())
            self.userID = userID
            self.active = True
            openFile.close()
        except:
            raise InvalidLogin

    def acceptFriend(self, friend: User):
        self.user.friendsList[friend.userID] = friend

    def declineFriend(self, friend: User):
        None

    def sendFriendRequest(self, friend: User):
        pass

    def removeFriend(self, friend: User):
        del self.user.friendsList[friend.userID]

    def showFriendList(self):
        for friend in self.friendsList.values():
            # display friend list
            pass

    def deleteAccount(self):
        self.auth.delete_user_account(self.user.userInstance['idToken'])

    def logOut(self):
        self.saveChanges

    # This will reformat the User file in storage with updated data
    def saveChanges(self):
        self.user.addToStorage()


#Below are 3 excxeptions for invalid username, passwords, and phone numbers
class InvalidUsername(Exception):

    def __init__(self, message='Invalid Username (MUST be between 7-30 alphanumeric characters)'):
        super().__init__(message)

class InvalidPassword(Exception):

    def __init__(self, message='Invalid Password (MUST be between 7-30 alphanumeric characters)'):
        super().__init__(message)

class InvalidPhoneNumber(Exception):

    def __init__(self, message='Invalid Phone Number (MUST be a valid 10 digit number)'):
        super().__init__(message)

#Invalid login
class InvalidLogin(Exception):

    def __init__(self, message='Invalid Login'):
        super().__init__(message)

# messy testing stuff disregard

# cal = Calendar()
# cal.taskList == {}
# cal.myCal != {}
# cal.taskList == {}
# cal.myCal[2022] != {}
# cal.myCal[2022][1] != {}
# cal.myCal[2022][1][1] == []

# # Ensures that an event can be added properly.
# firstTime = datetime.datetime(2022, 1, 1, 9)
# sTime = datetime.datetime(2022, 1, 1, 11)
# testEvent = Event(firstTime, sTime, "First Event", "1927 Orrington Avenue", "Video Call")
# testEvente = Event(firstTime, sTime, "First Even", "1927 Orrington Avenue", "Video Call")
# cal.addEvent(testEvent)
# cal.myCal[2022][1][1][0] == testEvent
# cal.myCal[2022][1][1][0].description == "Video Call"
# cal.displayDay(datetime.datetime(2022, 1, 1)) == [testEvent]
# cal.showAvailibility(firstTime, datetime.datetime(2022, 1, 3)) == [testEvent]

# secondTime = datetime.datetime(2022, 1, 2, 13)
# tTime = datetime.datetime(2022, 1, 2, 15)
# recurrance = Recurring("DAILY", 2, datetime.datetime(2022, 2, 1))
# secEvent = Event(secondTime, tTime, "Nap Time", "My bed", "Sleeping", recurrance)
# cal.addEvent(secEvent)
# cal.myCal[2022][1][8][0] == secEvent
# cal.myCal[2022][1][2][0] == secEvent
# cal.myCal[2022][1][30][0] == secEvent
# # print(cal.myCal[2022])

# email = "joshuachio10@gmail.com"
# password = "JoshuaChio1020"

# # u = User("Joshua Chio", email, password, cal, 9725911128)
# # u.addToStorage()

# f = Session('testingAccount@gmail.com', 'testing123')
# print(f.user.userInstance)
# f.deleteAccount()
# print(f.user.username)
# f.user.setUsername("changed")
# f.user.calendar.addEvent(testEvente)
# events = f.user.calendar.showAvailibility(firstTime, datetime.datetime(2022, 1, 20))
# for e in events:
#     print(e.event_name)
# print()
# f.logOut()

# # g = Session('joshuachio10@gmail.com', 'JoshuaChio1020')
# # print(g.user.username)
