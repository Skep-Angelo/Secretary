import json
import uuid
from DateTime.date_rep_prot import TimeIntervalRepresentation, subtract_time_points, add_time_time, add_to_timeRep

# Read JSON
with open("Functions\Task_object_all.json", 'r') as f:
    data_buffer = json.load(f)

# iterate over all task
for data in data_buffer["tasks"]:
    # if status is assigned, skip,
    if data["status"] == "assigned":
        continue

    # and if status is pending, attempt to assign

    # duration: infinite or defined

    # add to timetable block if unsplittable
    '''
        in attempt to assign
        check time to occupy
        if available, assign
        if not available, is the task movable, assign
        or if the task taking the position is movable
        if not all, return cannot assign
    '''

    # variables required
    task_id = data["id"]
    editable = data["editable"]

    # add to timetable block if splittable
    # splittable has to be defined; week, day, monthly

    # split the time in a given period or based
    # on pre given time
    def write(timing):
        # Read JSON
        with open('Json\Active_tasks.json', 'r') as f:
            dataWrite = json.load(f)

        # Modify data
        new_task = {"block_id": str(uuid.uuid4()), "task_id": task_id, "editable": editable, "timing": timing}
        dataWrite[timing[0]].append(new_task)

        # Write back
        with open('Json\Active_tasks.json', 'w') as f:
            json.dump(dataWrite, f, indent=4)



    '''These are the variables upon which computation will be performed before transfer into active tasks'''
    timespan = TimeIntervalRepresentation(data["timing"][0])

    timespan_duration = timespan.duration()
    timespan_period = timespan.period()
    timespan_cycles = timespan.cycle()

    total_duration = data["timing"][1]
    focus_duration = data["timing"][2]

    task_occurence = total_duration // focus_duration
    if total_duration > timespan_duration:
        raise "Error, cannot perform task under time constraint"
    elif abs(timespan_duration - total_duration) < 5:
        write([timespan.start_time(), timespan.end_time()]) # start to end of timespan
    elif abs(timespan_period - 1) < 1:
        start = timespan.start_time()

        interval = timespan_duration / task_occurence

        times = []

        for iter in range(0, task_occurence):
            starter = start + (iter * interval)
            times.append([starter, add_time_time(starter, focus_duration)])

        for timings in times:
            write(timings)
    else:
            a = timespan_cycles / task_occurence
            times = []

            starting_time = timespan.start_time()
            
            times.append([starting_time, timespan.start_time() + a*timespan_period])
            for i in range(0, task_occurence):
                step = add_to_timeRep(starting_time, (a*timespan_period), )
                times.append([starting_time, step])
                starting_time = step
                
            for timings in times:
                write(timings) # skip count by a

              

        









