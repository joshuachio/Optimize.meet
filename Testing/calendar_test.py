from .context import Source
from Source import be_calendar, be_events, be_recurring, be_tasks
import pytest
import datetime


def test_init():
    #Ensures that INIT functions properly.
    cal = be_calendar.Calendar()
    assert cal.taskList == {}
    assert cal.myCal != {}
    assert cal.taskList == {}
    assert cal.myCal[2022] != {}
    assert cal.myCal[2022][1] != {}
    assert cal.myCal[2022][1][1] == []

    #Ensures that an event can be added properly. 
    firstTime = datetime.datetime(2022,1, 1, 9)
    sTime = datetime.datetime(2022,1, 1, 11)
    testEvent = be_events.Event(firstTime, sTime, "First Event", "1927 Orrington Avenue", "Video Call")
    assert cal.addEvent(testEvent) == None
    assert cal.myCal[2022][1][1][0] == testEvent
    assert cal.myCal[2022][1][1][0].description == "Video Call"
    assert cal.displayDay(datetime.datetime(2022,1,1)) == [testEvent]
    assert cal.showAvailibility(firstTime, datetime.datetime(2022,1, 3)) == [testEvent]

    secondTime = datetime.datetime(2022,1, 2, 13)
    tTime = datetime.datetime(2022,1, 2, 15)
    recurrance = be_recurring.Recurring("DAILY", datetime.datetime(2022, 2, 1), 2)
    secEvent = be_events.Event(secondTime, tTime, "Nap Time", "My bed", "Sleeping", recurrance)
    assert cal.addEvent(secEvent) == None
    assert cal.myCal[2022][1][8][0] == secEvent
    assert cal.myCal[2022][1][2][0] == secEvent
    assert cal.myCal[2022][1][30][0] == secEvent

    thirdTime = datetime.datetime(2022, 3, 2, 13)
    thTime = datetime.datetime(2022, 3, 2, 15)
    recurrance2 = be_recurring.Recurring("WEEKLY", datetime.datetime(2022, 4, 2), 1, [1, 3, 4])
    thirdEvent = be_events.Event(thirdTime, thTime, "Sleep", "My bed", "Napping", recurrance2)
    assert cal.addEvent(thirdEvent) == None
    assert cal.myCal[2022][3][2][0] == thirdEvent
    assert cal.myCal[2022][3][3][0] == thirdEvent
    assert cal.myCal[2022][3][14][0] == thirdEvent
    assert cal.myCal[2022][3][16][0] == thirdEvent
    assert cal.myCal[2022][3][24][0] == thirdEvent
    assert cal.myCal[2022][3][25] == []
    assert cal.myCal[2022][4][2] == []

    assert cal.displayTaskList(datetime.datetime(2022,1,1)) == []
    due = datetime.datetime(2022, 1, 2)
    task1 = be_tasks.Task("ECE HW", due)
    assert cal.addTask(task1) == None
    assert cal.displayTaskList(due) == [task1]
    assert cal.dailyDigest(due) == [secEvent]
    assert cal.removeTask(task1) == None
    assert cal.displayTaskList(due) == []
    assert cal.taskList[due.date] == []


    assert cal.deleteEvent(testEvent) == None
    assert cal.myCal[2022][1][1] == []
    assert cal.deleteEvent(secEvent) == None
    assert cal.myCal[2022][1][8] == []
    assert cal.myCal[2022][1][2] == []
    assert cal.myCal[2022][1][30] == []
    assert cal.displayDay(datetime.datetime(2022,1,1)) == []
    assert cal.displayTaskList(datetime.datetime(2022,1,1)) == []
    assert cal.showAvailibility(datetime.datetime(2022,1,1), datetime.datetime(2022,1,1)) == []
    assert cal.dailyDigest(due) == []
