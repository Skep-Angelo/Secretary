import json

def remove_tasks_by_fields(criteria: dict, filename='tasks.json'):
    """
    Remove tasks that match ALL the field-value pairs in criteria.
    
    Args:
      criteria (dict): Fields and their values to match for removal.
      filename (str): JSON file path.
    
    Example:
      remove_tasks_by_fields({'name': 'Write report'})
      remove_tasks_by_fields({'name': 'Write report', 'priority': 'high'})
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    
    def matches(task):
        # Check if ALL criteria fields match in the task
        return all(task.get(key) == value for key, value in criteria.items())
    
    # Keep only tasks that do NOT match criteria
    filtered_tasks = [task for task in data['tasks'] if not matches(task)]
    
    data['tasks'] = filtered_tasks
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


# Usage examples:
remove_tasks_by_fields({'name': 'Write report'})  # removes all tasks named "Write report"
remove_tasks_by_fields({'name': 'Write report', 'priority': 'high'})  # removes tasks matching both
