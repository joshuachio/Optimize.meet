
import time
import numpy
import calendar


class Day:

class Event:
   
    def __init__(self, start_time, end_time, start_date, end_date, event_name, recurring, description):
        self.start_time = start_time
        self.end_time = end_time
        self.start_date = start_date
        self.end_date = end_date
        self.event_name = event_name
        self.recurring = recurring #needs to be a "recurring type" with weekly/daily/etc
        self.description = description

class Course(Event):

   def __init__(self, start_time, end_time, start_date, end_date, event_name, recurring, description):
       super().__init__(start_time, end_time, start_date, end_date, event_name, recurring, description)
       self.



class Meeting(Event):

   def __init__(self, start_time, end_time, start_date, end_date, event_name, recurring, description):
       super().__init__(start_time, end_time, start_date, end_date, event_name, recurring, description)
       self.


class Personal(Event):

   def __init__(self, start_time, end_time, start_date, end_date, event_name, recurring, description):
       super().__init__(start_time, end_time, start_date, end_date, event_name, recurring, description)
