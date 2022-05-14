import calendar
import pytest
import datetime



def test_init():
    cal = calendar.Calendar()
    #assert (cal.taskList) == {}
    assert cal.calendar != {}
    assert cal.calendar[2022] != {}
    assert cal.calendar[2022][1] != {}
    assert cal.calendar[2022][1][datetime.datetime(2022,1,1)] == []


