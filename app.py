import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"


class TaskManager:
    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            return json.load(f)

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, title, description):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()
        return task

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                return task
        return None

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        self.save_tasks()


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b


def show_menu():
    print("\n=== Task Manager & Calculator App ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Calculator")
    print("6. Exit")


def calculator_menu():
    calc = Calculator()
    print("\n--- Calculator ---")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = input("Choose operation: ")

    if choice == "1":
        print("Result:", calc.add(a, b))
    elif choice == "2":
        print("Result:", calc.subtract(a, b))
    elif choice == "3":
        print("Result:", calc.multiply(a, b))
    elif choice == "4":
        print("Result:", calc.divide(a, b))
    else:
        print("Invalid choice")


def main():
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            desc = input("Enter description: ")
            task = manager.add_task(title, desc)
            print("Task added:", task)

        elif choice == "2":
            tasks = manager.list_tasks()
            if not tasks:
                print("No tasks found.")
            for t in tasks:
                status = "Done" if t["completed"] else "Pending"
                print(f"{t['id']}. {t['title']} - {status}")

        elif choice == "3":
            task_id = int(input("Enter task ID to complete: "))
            task = manager.complete_task(task_id)
            if task:
                print("Task marked as completed.")
            else:
                print("Task not found.")

        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
            print("Task deleted.")

        elif choice == "5":
            calculator_menu()

        elif choice == "6":
            print("Exiting application.")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
