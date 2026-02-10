class DateRepresentation:
    def __init__(self, datetimerepresentation: str):
        year, month, date, day, time = map(int, datetimerepresentation.split(" "))
        self.year = year
        self.month = month
        self.date = date
        self.day = day
        self.time = time
        self.time_values = [self.year, self.month, self.date, self.day, self.time]

    def formatted(self):
        pass

    def start_time(self):
        time = []
        for i in self.time_values:
            if isinstance(i, list):
                time.append(i[0])
            else:
                time.append(i)

    def end_time(self):
        pass

    def num_rep(self):
        return [self.year, self.month, self.date, self.day, self.time]

    def duration(self):
        return self.end_time.num_rep() - self.start_time.num_rep()