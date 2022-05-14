import be_calendar
import pytest
import datetime



def test_init():
    cal = be_calendar.Calendar()
    assert (cal.taskList) == {}
    assert cal.myCal != {}
    assert cal.myCal[2022] != {}
    assert cal.myCal[2022][1] != {}
    assert cal.myCal[2022][1][datetime.datetime(2022,1,1)] == []


