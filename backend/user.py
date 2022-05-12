import datetime
from calendar import Calendar

class User:
    def __init__(self, username, email, password, calendar: Calendar, phoneNumber = None):
        self.username = username
        self.email = email
        self.calendar = calendar
        self.phoneNumber = phoneNumber

    def 