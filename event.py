class Event:
    def __init__(self, category, date, start_time, location, age_restrict):
        self.category = category
        self.date = date
        self.start_time = start_time
        self.location = location
        self.age_restrict = age_restrict

    def __str__(self):
        return f"this category: {self.category} is held in {self.date} and starts at {self.start_time}, the event is " \
               f"age restricted  and only {self.age_restrict} years or older attend this show"
