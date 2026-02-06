import uuid
import json
from datetime import datetime, timezone


def accept_task(name, type, earliest_start, specific_start_time, 
                deadline, deadline_type, duration_minutes, priority, occurrence, 
                movable, splittable, energy, category, buffer_before, buffer_after, status):
    # ______________________________task id generation______________________________

    task_id = str(uuid.uuid4())


    # ______________________________created at assignment______________________________
    # Get current time in UTC
    now = datetime.now(timezone.utc)

    # Format as ISO 8601 string with 'Z' for UTC
    created_at = now.strftime('%Y-%m-%dT%H:%M:%SZ')



    # ______________________________addition to task list______________________________________

    # Read JSON
    with open('data.json', 'r') as f:
        data = json.load(f)

    # Modify data
    new_task = {"id": task_id, "name": name, "created_at": created_at, "type": type,
                "earliest_start": earliest_start, "specific_start_time": specific_start_time,
                "deadline": deadline, "deadline_type": deadline_type,
                "duration_minutes": duration_minutes, "priority": priority,
                "occurrence": occurrence, "movable": movable, "splittable": splittable,
                "energy": energy, "category": category, "buffer_before": buffer_before,
                "buffer_after": buffer_after, "status": status}
    data['tasks'].append(new_task)

    # Write back
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)