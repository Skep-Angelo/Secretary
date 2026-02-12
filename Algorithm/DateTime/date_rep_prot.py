class TimeIntervalRepresentation:
    import calendar
    def __init__(self, datetimerepresentation: str):
        year, month, date, day, time = map(str, datetimerepresentation.split(" "))
        self.year = year
        self.month = month
        self.date = date
        self.day = day
        self.time = time
        self.time_values = [self.year, self.month, self.date, self.day, self.time]
        for i in self.time_values:
            if ":" in list(i):
                if self.time_values.index(i) != 4:
                    self.time_values[self.time_values.index(i)] = list(range(int(i.split(":")[0]), int(i.split(":")[1]) + 1))
                else:
                    self.time_values[self.time_values.index(i)] = list(map(int, i.split(":")))
            if "," in list(i):
                if self.time_values.index(i) != 4:
                    self.time_values[self.time_values.index(i)] = set(list(map(int, i.split(","))))
                else:
                    raise ValueError("Has no duration")
        print(self.time_values)

    def start_time(self):
        time_start = []
        for i in self.time_values:
            if isinstance(i, list) and self.time_values.index(i) == 3:
                continue
            if isinstance(i, list):
                time_start.append(i[0])
            else:
                time_start.append(i)
        return time_start

    def end_time(self):
        time_end = []
        for i in self.time_values:
            if isinstance(i, list) and self.time_values.index(i) == 3:
                continue
            if isinstance(i, list):
                time_end.append(i[len(i) - 1])
            else:
                time_end.append(i)
        return time_end

    def duration(self):
        a = self.start_time()
        print(f"start time: {a}")
        b = self.end_time()
        print(f"end time: {b}")
        c = []

        import calendar

        year = 2026
        month = 2  # February

        # Get a calendar for the month (returns a list of weeks)
        month_calendar = calendar.monthcalendar(year, month)

        # Weekday constants: 0=Monday, 1=Tuesday, ..., 6=Sunday
        target_weekday = 2  # Wednesday (0=Mon, 1=Tue, 2=Wed, etc.)

        # Find all dates that are the target weekday
        dates_on_weekday = []
        for week in month_calendar:
            # week is a list of 7 days, where Monday=index 0, Sunday=index 6
            if week[target_weekday] != 0:  # 0 means day outside this month
                dates_on_weekday.append(week[target_weekday])

        print(f"All Wednesdays in Feb 2026: {dates_on_weekday}")

        c.append((len(self.time_values[0]))*365 if isinstance(self.time_values[0], list) else 0)
        c.append((len(self.time_values[1])%12)*30 if isinstance(self.time_values[1], list) else 0)
        c.append(len(self.time_values[2])%30 if isinstance(self.time_values[2], list) else 0)

        a = int(self.time_values[4][1]) - int(self.time_values[4][0]) if isinstance(self.time_values[4], list) else 0
        while len(list(str(a))) < 4:
            a = "0" + str(a)
        minute = str(list(str(a))[len(str(a))-2]) + str(list(str(a))[len(str(a))-1])
        hours = list(str(a))[0] + list(str(a))[1] if len(str(a)) == 4 else list(str(a))[0]
        time = float(hours) + float(minute)/60
        print(f"time: {time}")
        print(c)
        return sum(c)*time
    

    def num_rep(self, point):
        val = ""
        if point == "start":
            for i in self.start_time():
                val += str(i)
        elif point == "end":
            for i in self.end_time():
                val += str(i)
        return int(val)
    
    def subtract(self, other):
        return self.num_rep("start") - other.num_rep("start")
    
    def add(self, other):
        return self.num_rep("start") + other.num_rep("start")

a = TimeIntervalRepresentation("2026 12 25 5 1000:1200")
b = TimeIntervalRepresentation("2026 12 25 5 0000:2400")

print(a.num_rep("start") < b.num_rep("start"))