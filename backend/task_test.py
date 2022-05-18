from be_tasks import Task
import pytest
import datetime

def test_init():
    d = datetime.datetime(2022, 2, 4)
    task1 = Task("Do laundry", d)
    assert task1.description == ''
    assert task1.name == "Do laundry"
    assert task1.dueDate == d
    assert task1.done == False
    task1.finishedTask()
    assert task1.done == True
    task1.unfinishTask()
    assert task1.done == False

    task2 = Task("Go eat lunch", d, "Cook ramen")
    assert task2.description == 'Cook ramen'
    assert task2.name == "Go eat lunch"
    assert task2.dueDate == d