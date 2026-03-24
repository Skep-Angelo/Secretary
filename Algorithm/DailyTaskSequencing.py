from datetime import datetime, timedelta
import json

# check today's date,
# check for 
#       uncompleted yesterday's
#       infinite timespan tasks
# tasks and move to today's tasks

# make the timetable 

# start with the earliest task by writing in the daily timetable
# move to start of time for the day
# next is the second earliest task
# if coincides with the previous task including the buffer,
# shift either the instance or the previous (one which is editable) till it fits,
# if both not editable, split the splittable, else raise an error

def add_hours_to_time_list(time_list, hours_to_add):
    dt = datetime(*time_list)
    new_dt = dt + timedelta(hours = hours_to_add)
    return [new_dt.year, new_dt.month, new_dt.day, new_dt.hour, new_dt.minute, new_dt.second]

def shifting_time_interval(time_array, hours_to_add, editable):
    if editable[1]:
        dt = datetime(*time_array[0])
        new_dt = dt + timedelta(hours = hours_to_add)

        dt2 = datetime(*time_array[1])
        new_dt2 = dt2 + timedelta(hours=hours_to_add)

        return [[new_dt.year, new_dt.month, new_dt.day, new_dt.hour, new_dt.minute, new_dt.second], [new_dt2.year, new_dt2.month, new_dt2.day, new_dt2.hour, new_dt2.minute, new_dt2.second]]
    else:
        raise("Uneditable")

def start_task():
    pass

#check for today's date and parse in the stored way
#########################################################
today = datetime.now()
yesterday = today - timedelta(days=1)

todayDate = today.strftime("%Y%m%d")
yesterdayDate = yesterday.strftime("%Y%m%d")




# Move all uncompleted tasks from yesterday to today
##########################################################
with open("Json\\Active_tasks2.json", 'r') as f:
    data_buffer = json.load(f)

if yesterdayDate in data_buffer:
    # iterate over all task
    for data in data_buffer[yesterdayDate]:
        # if state is completed, skip,
        if data["state"] == "completed":
            continue
        else:
            block_id = data["block_id"]
            task_id = data["task_id"]
            editable = data["editable"]
            timing = data["timing"]

            # Read JSON
            with open('Json\\Active_tasks2.json', 'r') as f:
                dataWrite = json.load(f)

            # Modify data
            new_task = {"block_id": block_id, "task_id": task_id, "editable": editable, "timing": timing, "state":"uncompleted"}
            dataWrite.setdefault(todayDate, []).append(new_task)

            # Write back
            with open('Json\\Active_tasks2.json', 'w') as f:
                json.dump(dataWrite, f, indent=1)


# arrangement of tasks according to the starting times (ascending order)
#############################################################
with open('Json\\Active_tasks2.json', 'r') as f:
    dataWriteSort = json.load(f)
print(todayDate)
sorted_data = sorted(dataWriteSort[todayDate], key=lambda x:x['timing'])
with open('Json\\Active_tasks2.json', 'w') as f:
    json.dump(sorted_data, f, indent=1)



# should be done 12 midnight everyday
############################################################
timestart = [9, 0, 0]
endtime = [20, 0, 0]
buff = 0.4


with open('Json\\Active_tasks2.json', 'r') as f:
    dataWrite2 = json.load(f)

times = [[item["block_id"], item["timing"], item["editable"]] for item in dataWrite2 if "timing" in item]

finalSchedule = []

for iter in range(0, len(times)):
    if times[iter][2] == [False, False]:
        finalSchedule.append(times[iter])

for iter2 in range(0, len(times)):
    start = times[iter2][1][0]
    end = times[iter2][1][1]
    editable = times[iter2][2]

    placed = False

    start = datetime(*start)
    end = datetime(*end)

    for i, fixed in enumerate(finalSchedule):
        Sstart = fixed[1][0]
        Send = fixed[1][1]
        editable2 = fixed[2]

        Sstart = datetime(*Sstart)
        Send = datetime(*Send)
        duration = ((end - start).total_seconds())/3600

        # shifting, splittable

        if ((start > Sstart and start < Send) or (end > Sstart and end < Send)) or (start < Sstart and end > Send):
            print("coinciding partially")
            if editable2[0] or (end > Send and start > Sstart) or ((start >= Sstart and start <= Send) and (end >= Sstart and end <= Send)):
                start = Send
                end = start + timedelta(hours = duration)

            elif editable2[1]:
                if (Sstart - start).total_seconds()/3600 > 0.4:
                    ranVar = Sstart-timedelta(hours = buff)
                    finalSchedule.insert(i, [times[iter2][0], [[start.year, start.month, start.day, start.hour, start.minute, start.second], [ranVar.year, ranVar.month, ranVar.day, ranVar.hour, ranVar.minute, ranVar.second]], times[iter2][2]])
                    newStart = Send + timedelta(hours = buff)
                    durSub = ((ranVar - start).total_seconds())/3600
                    newEnd = newStart + timedelta(hours=(buff) + (duration-durSub))
                    times.insert(i+1, [times[iter2][0], [[newStart.year, newStart.month, newStart.day, newStart.hour, newStart.minute, newStart.second], [ranVar.year, ranVar.month, ranVar.day, ranVar.hour, ranVar.minute, ranVar.second]], times[iter2][2]])
                    placed = True
                    break
                else:
                    start = Send
                    end = start + timedelta(hours = duration)

                    
    if not placed:
        finalSchedule.append([times[iter2][0], [[start.year, start.month, start.day, start.hour, start.minute, start.second], [end.year, end.month, end.day, end.hour, end.minute, end.second]], times[iter2][2]])
        finalSchedule.sort(key=lambda x:x[1][0])

print(finalSchedule)


'''def conditionInDayTime(date):
    start_time = [date[0][0], date[0][1], date[0][2], timestart[0:2]]
    end_time = [date[0][0], date[0][1], date[0][2], end_time[0:2]]

    st = datetime(*start_time)
    ed = datetime(*end_time)

    st_date = datetime(*date[0])
    ed_date = datetime(*date[1])

    state = True
    typ = ''
    if st_date < st:
        state = False
        typ = 0
    if ed_date > ed:
        state = False
        typ = 1
    if st_date < st and ed_date > ed:
        state = False
        typ = 2

    return [state, typ]

for i in times:
    ##############################################
    # shifting into work time
    res = conditionInDayTime()
    if res[0]:
        pass
    else:
        if res[1] == 0:
            shifting_time_interval()
        else:
            shifting_time_interval()

    ##############################################
    # checking for cohesion with any task

    
    
with open('Json\\Active_tasks2.json', 'w') as f:
    json.dump(sorted_data, f, indent=1)'''

