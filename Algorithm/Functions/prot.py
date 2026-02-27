import json
import uuid
from DateTime.date_rep_prot import TimeIntervalRepresentation

# iterate over all task
# Read JSON
with open('data.json', 'r') as f:
    data = json.load(f)
# if status is assigned, skip,
if data["status"] == "assigned":
    pass

# and if status is pending, attempt to assign

# duration: infinite or defined

# add to timetable block if unsplittable
'''
    in attempt to assign
    check time to occupy
    is the time available
    if available, assign
    if not available, is the task movable, assign
    or if the task taking the position is movable
    if not all, return cannot assign
'''

# add to timetable block if splittable
# splittable has to be defined; week, day, monthly

# split the time in a given period or based
# on pre given time


'''Focus more on repetitive tasks
the total span is continuous
the duration is less than total span
the focus time is less than total span'''
# find the total number of times it should be done,
# given the focus time and the total duration.
numberOfCounts = round(data["timing"][1] // data["timing"][2]) # total duration/focus time

# frequency of task
frequency = data["timing"][0] // numberOfCounts # minutes

# for every "frequency" the task should be done once
# write in the task accepted at the start of span + buffer
# timespan(task to succeding task), editable,

time_buff = "startime"
task_mem =[]
for iter in range(1, numberOfCounts):
    bid = []
    bid.append(time_buff)
    time_buff += frequency
    bid.append(time_buff)
    task_mem.append(bid)

for step in range(0, len(task_mem)):
    timeInter = task_mem[step]
    string_rep = ""
    start_rep = timeInter[0].split(" ")
    end_rep = timeInter[1].split(" ")
    for m in range(0, len(start_rep) - 1):
        if start_rep[m] == end_rep[m]:
            string_rep =+ f"{start_rep[m]} "
        else:
            string_rep =+ f"{start_rep[m]}:{end_rep[m]} "
    task_mem[step] = string_rep


# Read JSON
with open('active_tasks.json', 'r') as f:
    dataWrite = json.load(f)

# Modify data
for i in task_mem:
    new_task = {"block_id": str(uuid.uuid4()), "task_id": data["id"], "editable": "category", "timespan": TimeIntervalRepresentation(task_mem), "buffer": 30}
    dataWrite['tasks'].append(new_task)

# Write back
with open('data.json', 'w') as f:
    json.dump(dataWrite, f, indent=4)







