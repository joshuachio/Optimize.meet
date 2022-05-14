import datetime

byDay = {
    7: "SUNDAY",
    1: "MONDAY",
    2: "TUESDAY",
    3: "WEDNESDAY",
    4: "THURSDAY",
    5: "FRIDAY",
    6: "SATURDAY"
}

class Recurring:

    def __init__(self, freq: str, interval: int, endDate: datetime.datetime, byDay: list[int] = None, count = None):
        self.setFreq(freq)
        self.interval = interval
        self.endDate = endDate
        self.setByDay(byDay)
        self.count = count

    #Checks valid freq
    def setFreq(self, freq):
        if freq == "DAILY" or freq == "WEEKLY":
            self.freq = freq
        else:
            self.freq = None

    #Checks that the int is a valid day according to the byDay dict
    def setByDay(self, byDay):
        self.byDay = []
        for i in byDay:
            if 0 < i < 8:
                self.byDay.append(i)

