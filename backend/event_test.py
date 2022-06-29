from be_events import Event, Course, Meeting, Personal
from be_recurring import Recurring
import pytest
import datetime



def test_init():
    testStartDate = datetime.datetime(2022, 1, 1, 19, 0) #9 am Jan 1st, 2022
    testEndDate = datetime.datetime(2022, 1, 1, 11, 0) #11 am Jan 1st, 2022
    event = Event(testStartDate, testEndDate, "call Ethan", "1234 Road", "Discuss calendar project")
    event.setDescription("Discuss calendar app")
    assert event.description == "Discuss calendar app"
    recurrance = Recurring("WEEKLY", 2, datetime.datetime(2022, 2, 1))
    event1 = Event(testStartDate, testEndDate, "party on Ethan's bed", "1234 Road", "very fun stuff", recurrance, False)
    assert event1.recurring == recurrance
    