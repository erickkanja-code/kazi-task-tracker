
tasks = []
next_task_id = 1


def add_task(title):
    global next_task_id

    if not title or not title.strip():
        print("Error: Task title cannot be empty.")
        return

    task = {
        "id": next_task_id,
        "title": title.strip(),
        "status": "pending"
    }

    tasks.append(task)
    next_task_id += 1

    print(f"Task added successfully: {task['title']}")


def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Task {task_id} deleted successfully.")
            return

    print(f"Error: Task with ID {task_id} does not exist.")
