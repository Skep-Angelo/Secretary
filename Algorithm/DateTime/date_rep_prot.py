# Time Representation class

class TimeIntervalRepresentation:
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
            if i == "*":
                if self.time_values.index(i) == 0:
                    self.time_values[self.time_values.index(i)] = list(range(2026, 10000))
                elif self.time_values.index(i) == 1:
                    self.time_values[self.time_values.index(i)] = list(range(1, 13))
                elif self.time_values.index(i) == 2:
                    self.time_values[self.time_values.index(i)] = list(range(1, 32))
                elif self.time_values.index(i) == 3:
                    self.time_values[self.time_values.index(i)] = list(range(0, 7))
                elif self.time_values.index(i) == 4:
                    self.time_values[self.time_values.index(i)] = list(range(0, 24))
        print(f" time rep = {self.time_values}")

    def check_date_day(self, year, month, dates, weekday, state):
        import calendar

        if not isinstance(year, list):
            year = [year]

        if not isinstance(month, list):
            month = [month]

        if not isinstance(dates, list):
            dates = [dates]

        if not isinstance(weekday, list):
            weekday = [weekday]

        if state == "begin":
            for years in year:
                for days in weekday:
                    for month_index in month:
                            for date_index in dates:
                                month_calendar = calendar.monthcalendar(int(years), int(month_index))
                                dates_on_weekday = []
                                for week in month_calendar:
                                    if week[int(days)] != 0:
                                        dates_on_weekday.append(week[int(days)])
                                if int(date_index) in dates_on_weekday:
                                    return [True, month_index, date_index]
            return [False]
        else:
            for years in year[::-1]:
                for days in weekday[::-1]:
                    for month_index in month[::-1]:
                        for date_index in dates:
                            month_calendar = calendar.monthcalendar(int(years), int(month_index))
                            dates_on_weekday = []
                            for week in month_calendar:
                                if week[int(days)] != 0:
                                    dates_on_weekday.append(week[int(days)])
                                if int(date_index) in dates_on_weekday:
                                    return [True, month_index, date_index]
            return [False]

    def start_time(self):
        time_start = []
        for i in self.time_values:
            if self.time_values.index(i) == 1:
            ##################################################
                check = self.check_date_day(self.time_values[0], self.time_values[1], self.time_values[2], self.time_values[3], "begin")
                if not check[0]:
                    raise ValueError("Date does not match the day of the week")
                else:
                    time_start.append(check[1])
                    time_start.append(check[2])
            ################################################
            else:
                if self.time_values.index(i) == 2 or self.time_values.index(i) == 3:
                    continue
                if isinstance(i, list):
                    time_start.append(i[0])
                else:
                    time_start.append(i)
        return time_start

    def end_time(self):
        time_end = []
        for i in self.time_values:
            if self.time_values.index(i) == 1:
            ##################################################
                check = self.check_date_day(self.time_values[0], self.time_values[1], self.time_values[2], self.time_values[3], "end")
                if not check[0]:
                    raise ValueError("Date does not match the day of the week")
                else:
                    time_end.append(check[1])
                    time_end.append(check[2])
            ################################################
            else:
                if self.time_values.index(i) == 2 or self.time_values.index(i) == 3:
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
            print(f"start time: {self.start_time()}")
            for i in self.start_time():
                if self.start_time().index(i) == 1 or self.start_time().index(i) == 2:
                    while len(str(i)) < 2:
                        i = "0" + str(i)
                elif self.start_time().index(i) == 4:
                    while len(str(i)) < 4:
                        i = "0" + str(i)
                val += str(i)
        elif point == "end":
            print(f"end time: {self.end_time()}")
            for i in self.end_time():
                if self.end_time().index(i) == 1 or self.end_time().index(i) == 2:
                    while len(str(i)) < 2:
                        i = "0" + str(i)
                elif self.end_time().index(i) == 4:
                    while len(str(i)) < 4:
                        i = "0" + str(i)
                val += str(i)
        return int(val)
    
    def subtract(self, other):
        return self.num_rep("start") - other.num_rep("start")
    
    def add(self, other):
        return self.num_rep("start") + other.num_rep("start")

def subtract_time_points(time, start_end, year=0, month=0, date=0, time_point=0):
    # extract the start time or end time from the time interval representation
    # time.start_time returns a list of [year, month, date, time in minutes]
    if isinstance(time, TimeIntervalRepresentation):
        val = time.start_time()
    else:
        val = time if time is not list else time.split(" ")
    def reduce_year(var):
        nonlocal year
        if val[0] - year < 0:
            raise ValueError("Cannot subtract more years than the start or end time has")
        else:
            val[0] -= var

    def reduce_month(var):
        nonlocal month
        if val[1] - month < 0:
            reduce_year(month//12 + 1)
            val[1] -= month%12
        else:
            val[1] -= var

    def reduce_date(var):
        nonlocal date
        if val[2] - date < 0:
            reduce_month(date//30 + 1)
            val[2] -= date%30
        else:
            val[2] -= var

    def reduce_time(var):
        nonlocal time_point
        if val[4] - time_point < 0:
            reduce_date(time_point//2400 + 1)
            val[4] -= time_point%2400
        else:
            val[4] -= var

    for i in val:
        if val.index(i) == 0:
            reduce_year(year)
        elif val.index(i) == 1:
            reduce_month(month)
        elif val.index(i) == 2:
            reduce_date(date)
        elif val.index(i) == 4:
            reduce_time(time_point)
    ling = ":"
    # subtract time to "start or end" time and return new time interval representation
    ands = f"{val[0] if val[0] == time.start_time()[0] else val[0] }{ling}{time.end_time()[0]} {val[1] if val[1] == time.start_time()[1] else val[1]} {val[2] if val[2] == time.start_time()[2] else val[2]} {time.start_time()[3]} {val[4] if val[4] == time.start_time()[4] else val[4]}"
    # get the start time or end time
    # add time to it
    # merge with end time or start time
    # rewrite the variable with the new time interval representation

def add_time_points(time1, start_end):
    pass
    # add time to "start or end" time and return new time interval representation
    # get the start time or end time
    # add time to it
    # merge with end time or start time
    # rewrite the variable with the new time interval representation

def shift_time_point(time, shift):
    if shift < 0:
        subtract_time_points(time, "start")
        subtract_time_points(time, "end")
    else:
        add_time_points(time, "start")
        add_time_points(time, "end")
    # add time to start and end time and return new time interval representation


b = TimeIntervalRepresentation("2026 1:3 9:16 0:5 0000:2400")


print(b.num_rep("start"))
