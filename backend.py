class Event:
    def __init__(self, start_time, end_time, start_date, end_date, event_name, recurring, description) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.start_date = start_date
        self.end_date = end_date
        self.event_name = event_name
        self.recurring = recurring #needs to be a "recurring type" with weekly/daily/etc
        self.description = description

    
