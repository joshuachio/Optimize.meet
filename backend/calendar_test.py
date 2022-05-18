
import be_calendar
import pytest
import datetime
from be_events import Event
from be_recurring import Recurring


def test_init():
    cal = be_calendar.Calendar()
    assert (cal.taskList) == {}
    assert cal.myCal != {}
    assert cal.taskList == {}
    assert cal.myCal[2022] != {}
    assert cal.myCal[2022][1] != {}
    assert cal.myCal[2022][1][1] == []


    firstTime = datetime.datetime(2022,1, 1, 9)
    sTime = datetime.datetime(2022,1, 1, 11)
    testEvent = Event(firstTime, sTime, "First Event", "1234 Road", "Video Call")
    assert cal.addEvent(testEvent) == None
    assert cal.myCal[2022][1][1][0] == testEvent
    assert cal.myCal[2022][1][1][0].description == "Video Call"

    secondTime = datetime.datetime(2022,1, 2, 13)
    tTime = datetime.datetime(2022,1, 2, 15)
    recurrance = Recurring("DAILY", 2, datetime.datetime(2022, 2, 1))
    secEvent = Event(secondTime, tTime, "Nap Time", "My bed", "Sleeping", recurrance)
    assert cal.addEvent(secEvent) == None
    assert cal.myCal[2022][1][8][0] == secEvent
    assert cal.myCal[2022][1][2][0] == secEvent
    assert cal.myCal[2022][1][30][0] == secEvent

    assert cal.deleteEvent(testEvent) == None
    assert cal.myCal[2022][1][1] == []
    assert cal.deleteEvent(secEvent) == None
    assert cal.myCal[2022][1][8] == []
    assert cal.myCal[2022][1][2] == []
    assert cal.myCal[2022][1][30] == []

    assert cal.displayTaskList(datetime.datetime(2022,1,1)) == None
    assert cal.displayDay(datetime.datetime(2022,1,1)) == []
    assert cal.showAvailibility(datetime.datetime(2022,1,1), datetime.datetime(2022,1,1)) == []
    assert cal.dailyDigest() == []
