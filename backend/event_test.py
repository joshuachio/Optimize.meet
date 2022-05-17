from be_events import Event, Course, Meeting, Personal
import pytest
import datetime



def test_init():
    testStartDate = datetime.datetime(2022, 1, 1, 19, 0) #9 am Jan 1st, 2022
    testEndDate = datetime.datetime(2022, 1, 1, 11, 0) #11 am Jan 1st, 2022
    event = Event(testStartDate, testEndDate, "call Ethan", "1234 Road", "Discuss calendar project")
    event.setDescription("Discuss calendar app")
    assert event.description == "Discuss calendar app"