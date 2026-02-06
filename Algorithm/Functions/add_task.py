import uuid
import json
from datetime import datetime, timezone


def accept_task(name, category, timing, editable, buffer_time, importance, status):
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
    new_task = {"id": task_id, "name": name, "category": category, "created_at": created_at, "timing": timing,
                 "editable":editable, "buffer_time": buffer_time, "importance": importance, "status": status}
    data['tasks'].append(new_task)

    # Write back
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)