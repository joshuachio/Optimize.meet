import datetime
import jsonpickle
import pickle

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
        if byDay != None and self.freq == "WEEKLY":
            for i in byDay:
                if 0 < i < 8:
                    self.byDay.append(i)

Recurrance = Recurring("WEEKLY", 5, datetime.datetime(2022, 2, 1), [1, 2, 4])
# f = jsonpickle.encode(Recurrance)
# print(f)
# e = jsonpickle.decode(f)
# print(e.endDate)
p = pickle.dumps(Recurrance)
print(p)
q = pickle.loads(p)
print(q)
# print(json.dumps(str(Recurrance)))