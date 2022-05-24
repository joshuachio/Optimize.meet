import pytest
import datetime
import jsonpickle
import json
from collections import OrderedDict
from Pyrebase4 import pyrebase
from be_calendar import Calendar
from be_events import Event
from be_tasks import Task
from be_recurring import Recurring
from user_creation import User

# def test_init():
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

email = "joshuachio10@gmail.com"
password = "JoshuaChio1020"

u = User("Joshua Chio", email, password, cal, 9725911128)
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
storage = firebase.storage()
# # s = jsonpickle.encode(u)
# file = open('test.txt', 'w')
# print(s, file=file)
# file.close()
# u.userID
# storage.child("users/" + userID + ".txt").put('test.txt')

storage.child("users/" + u.userID + ".txt").download('download.txt', 'download.txt')
file = open('download.txt', 'r')
print(jsonpickle.decode(file.read()))