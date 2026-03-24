from datetime import datetime, timedelta

'''start_rep = [2023, 10, 27, 8, 30, 0]
constraint = []
end_rep = [2023, 10, 27, 15, 45, 0]

total_task_duration = 5
focus_duration = 0.5'''

def task_occurences(start_rep, constraint, end_rep, total_task_duration, focus_duration):
    if constraint == []:
        start_time = datetime(*start_rep)
        end_time = datetime(*end_rep)

        def add_hours_to_time_list(time_list, hours_to_add):
            dt = datetime(*time_list)
            new_dt = dt + timedelta(hours = hours_to_add)
            return [new_dt.year, new_dt.month, new_dt.day, new_dt.hour, new_dt.minute, new_dt.second]

        timespan = ((end_time - start_time).total_seconds())/3600
        #print(f"timespan {timespan}")

        if total_task_duration > timespan:
            raise("error")
        else:
            occur = total_task_duration / focus_duration
            no_period = (timespan - total_task_duration)/occur
            #print(occur)

        times = []

        for i in range(0, int(occur + 1)):
            buff = []
            buff.append(add_hours_to_time_list(start_rep, (focus_duration * i)  + (no_period * i)))
            buff.append(add_hours_to_time_list(buff[0], focus_duration))
            times.append(buff)

        #print(times)
        return times