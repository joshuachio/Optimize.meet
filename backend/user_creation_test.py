import pytest
import datetime
import jsonpickle
import json
from be_calendar import Calendar
from be_events import Event
from be_tasks import Task
from be_recurring import Recurring
from user_creation import User

def test_init():
    #Ensures initialization works
    username = 'testUser'
    email = "testingAccount@gmail.com"
    password = "testing123"
    cal = Calendar()
    phone = 1234567890
    testUser = User(username, email, password, cal, phone)
    assert testUser.username == 'testUser'
    assert testUser.password == password

    

    # u = User("Joshua Chio", email, password, cal, 9725911128)
    # config = {
    #             "apiKey": "AIzaSyAz5bLpUWAOBouA8Q9_WeloGYDdI1Q9s5g",
    #             "authDomain": "calendar-be058.firebaseapp.com",
    #             "databaseURL": "https://calendar-be058-default-rtdb.firebaseio.com",
    #             "projectId": "calendar-be058",
    #             "storageBucket": "calendar-be058.appspot.com",
    #             "messagingSenderId": "765432044481",
    #             "appId": "1:765432044481:web:7dceaf5af57e8374572d40",
    #             "measurementId": "G-9Q457P91BV"
    #         }
    # firebase = pyrebase.initialize_app(config)
    # storage = firebase.storage()
    # # # s = jsonpickle.encode(u)
    # # file = open('test.txt', 'w')
    # # print(s, file=file)
    # # file.close()
    # # u.userID
    # # storage.child("users/" + userID + ".txt").put('test.txt')

    # storage.child("users/" + u.userID + ".txt").download('download.txt', 'download.txt')
    # file = open('download.txt', 'r')
    # print(jsonpickle.decode(file.read()))