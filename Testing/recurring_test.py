from .context import Server
from Server.Source.be_recurring import Recurring
import pytest
import datetime

def test_init():
    failRecurrance = Recurring("BIMONTHLY", 2, datetime.datetime(2022, 2, 1))
    assert failRecurrance.freq == None
    assert failRecurrance.byDay == []
    Recurrance = Recurring("WEEKLY", 5, datetime.datetime(2022, 2, 1), [1, 2, 4])
    assert Recurrance.byDay == [1, 2, 4]
    Recurrance = Recurring("WEEKLY", 5, datetime.datetime(2022, 2, 1), [0, -1, 2, 4])
    assert Recurrance.byDay == [2, 4]
    NoDayRecurrance = Recurring("DAILY", 5, datetime.datetime(2022, 2, 1), [0, 2, 4])
    assert NoDayRecurrance.byDay == []
