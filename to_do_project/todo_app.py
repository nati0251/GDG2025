import json
import os

class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(data["id"], data["title"], data["completed"])

class TodoManager:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Task.from_dict(item) for item in data]
        except json.JSONDecodeError:
            return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title):
        new_id = max([t.id for t in self.tasks], default=0) + 1
        self.tasks.append(Task(new_id, title))
        self.save_tasks()

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]
        self.save_tasks()

    def Update_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = not task.completed
                break
        self.save_tasks()

def main():
    manager = TodoManager()

    while True:
        print("\n--- TODO APP ---")
        if not manager.tasks:
            print("No tasks available.")
        else:
            for task in manager.tasks:
                status = "✓" if task.completed else " "
                print(f"[{task.id}] [{status}] {task.title}")

        print("\nOptions: (1) Add (2) Update (3) Delete (4) Exit")
        choice = input("Select an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)

        elif choice == "2":
            tid = int(input("Enter Task ID to toggle: "))
            manager.Update_task(tid)

        elif choice == "3":
            tid = int(input("Enter Task ID to delete: "))
            manager.delete_task(tid)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
