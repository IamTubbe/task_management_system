# srp_tasks.py (เพิ่มส่วนนี้ที่ด้านบน)
from abc import ABC, abstractmethod

class TaskStorage(ABC):
   @abstractmethod
   def load_tasks(self):
       pass
   @abstractmethod
   def save_tasks(self, tasks):
       pass

# srp_tasks.py (ต่อจาก TaskStorage)

class FileTaskStorage(TaskStorage):
   def __init__(self, filename="tasks.txt"):
       self.filename = filename

   def load_tasks(self):
       loaded_tasks = []
       try:
           with open(self.filename, "r") as f:
               for line in f:
                   parts = line.strip().split(',')
                   if len(parts) == 4:
                       task_id = int(parts[0])
                       description = parts[1]
                       due_date = parts[2] if parts[2] != 'None' else None
                       completed = parts[3] == 'True'
                       loaded_tasks.append(Task(task_id, description, due_date, completed))
       except FileNotFoundError:
           print(f"No existing task file '{self.filename}' found. Starting fresh.")
       return loaded_tasks

   def save_tasks(self, tasks):
       with open(self.filename, "w") as f:
           for task in tasks:
               f.write(f"{task.id},{task.description},{task.due_date},{task.completed}\n")
       print(f"Tasks saved to {self.filename}")

# oop_tasks.py

class Task:
   def __init__(self, task_id, description, due_date=None, completed=False):
       self.id = task_id
       self.description = description
       self.due_date = due_date
       self.completed = completed

   def mark_completed(self):
       self.completed = True
       print(f"Task {self.id} '{self.description}' marked as completed.")

   def __str__(self):
       status = "✓" if self.completed else " "
       due = f" (Due: {self.due_date})" if self.due_date else ""
       return f"[{status}] {self.id}. {self.description}{due}"

# srp_tasks.py (ปรับปรุง TaskManager)

class TaskManager:
    def __init__(self, storage: TaskStorage):
        self.storage = storage
        self.tasks = self.storage.load_tasks()
        self.next_id = max([t.id for t in self.tasks] + [0]) + 1 if self.tasks else 1
        print(f"Loaded {len(self.tasks)} tasks. Next ID: {self.next_id}")

    def add_task(self, description, due_date=None):
        task = Task(self.next_id, description, due_date)
        self.tasks.append(task)
        self.next_id += 1
        self.storage.save_tasks(self.tasks)
        print(f"Task '{description}' added.")
        return task

    # เมธอดที่หายไป (ต้องเพิ่มกลับเข้าไป)
    def list_tasks(self):
        print("\n--- Current Tasks ---")
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(task)
        print("---------------------")

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def mark_task_completed(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_completed()
            self.storage.save_tasks(self.tasks)
            return True
        print(f"Task {task_id} not found.")
        return False


# srp_tasks.py (ปรับปรุง Logic หลัก)

if __name__ == "__main__":
   file_storage = FileTaskStorage("my_tasks.txt")
   manager = TaskManager(file_storage) # ส่ง FileTaskStorage เข้าไปเป็นอากิวเมนต์

   manager.list_tasks()
   manager.add_task("Review SOLID Principles", "2024-08-10")
   manager.add_task("Prepare for Final Exam", "2024-08-15")
   manager.list_tasks()
   manager.mark_task_completed(1)
   manager.list_tasks()
