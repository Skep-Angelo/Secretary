class DateRepresentation:
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
                self.time_values[self.time_values.index(i)] = list(range(int(i.split(":")[0]), int(i.split(":")[1]) + 1))

    def start_time(self):
        time_start = []
        for i in self.time_values:
            if isinstance(i, list):
                time_start.append(i[0])
            else:
                time_start.append(i)
        return time_start

    def end_time(self):
        time_end = []
        for i in self.time_values:
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

        c.append(((int(b[0]) - int(a[0])))*365)
        c.append((((int(b[1]) - int(a[1]))%12))*30)
        c.append((((int(b[2]) - int(a[2]))%30)))
        c.append((((int(b[3]) - int(a[3]))%7)))

        a = int(b[4]) - int(a[4])
        minute = str(list(str(a))[len(str(a))-2]) + str(list(str(a))[len(str(a))-1])
        hours = list(str(a))[0] + list(str(a))[1] if len(str(a)) == 4 else list(str(a))[0]
        time = float(hours) + float(minute)/60
        print(c)
        return sum(c)*time


a = DateRepresentation("2026 12 25 5 1000:1200")
b = DateRepresentation("2026 1 1:2 2 200:430")

print(b.duration())