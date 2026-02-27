import json
import uuid
from DateTime.date_rep_prot import TimeIntervalRepresentation, subtract_time_points, add_time_points

# Read JSON
with open('Task_object_all.json', 'r') as f:
    data_buffer = json.load(f)

# iterate over all task
for data in data_buffer["tasks"]:
    # if status is assigned, skip,
    if data["status"] == "assigned" or data_buffer.index(data) == 1:
        continue

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
    time_span = TimeIntervalRepresentation(data["timing"][0])
    numberOfCounts = round(data["timing"][1] // (data["timing"][2] + 2*data["buffer_time"])) # total duration/focus time

    # frequency of task
    frequency = time_span.duration() // numberOfCounts # minutes

    # for every "frequency" the task should be done once
    # write in the task accepted at the start of span + buffer
    # timespan(task to succeding task), editable,

    task_mem = []
    task_mem.append(time_span.start_time())
    for iter in range(0, numberOfCounts):
        task_mem.append(add_time_points(task_mem[iter], frequency))

    for step in range(0, len(task_mem)):
        string_rep = ""
        start_rep = task_mem[step]
        end_rep = task_mem[step + 1]
        for m in range(0, len(start_rep) - 1):
            if start_rep[m] == end_rep[m]:
                string_rep += f"{start_rep[m]} "
            else:
                string_rep += f"{start_rep[m]}:{end_rep[m]} "
        task_mem[step] = string_rep


    # Read JSON
    for indiv in task_mem:
        with open('active_tasks.json', 'r') as f:
            dataWrite = json.load(f)

        # Modify data
        for i in task_mem:
            new_task = {"block_id": str(uuid.uuid4()), "task_id": data["id"], "editable": [data["editable"][0], data["editable"][1]], "timespan": TimeIntervalRepresentation(task_mem)}
            dataWrite['tasks'].append(new_task)

        # Write back
        with open('data.json', 'w') as f:
            json.dump(dataWrite, f, indent=4)







