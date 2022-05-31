import pytest
import datetime
from be_calendar import Calendar
from be_events import Event
from be_tasks import Task
from be_recurring import Recurring
from user_creation import User, Session, InvalidUsername, InvalidPassword, InvalidPhoneNumber

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

    #Test logging into the account
    loginSession = Session(email, password)
    assert loginSession.user.userID == testUser.userID

    #Deletes this account
    assert testUser.deleteAccount() == None

    #Incorrect Username
    username = 't'
    email = "testingAccount2@gmail.com"
    password = "testing123"
    cal = Calendar()
    phone = 1234567890
    # assert User(username, email, password, cal, phone) == InvalidUsername()
    
def test_addToStorage():
    username = 'testUser2'
    email = "testingAccount2@gmail.com"
    password = "testing123"
    cal = Calendar()
    phone = 1234567890
    testUser = User(username, email, password, cal, phone)
    assert testUser.addToStorage() == None
    assert testUser.deleteAccount() == None