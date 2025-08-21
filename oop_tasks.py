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

# oop_tasks.py (ต่อจาก Class Task)

class TaskManager:
   def __init__(self):
       self.tasks = []
       self.next_id = 1

   def add_task(self, description, due_date=None):
       task = Task(self.next_id, description, due_date)
       self.tasks.append(task)
       self.next_id += 1
       print(f"Task '{description}' added.")
       return task

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
           return True
       print(f"Task {task_id} not found.")
       return False

# oop_tasks.py (ต่อจาก Class TaskManager)

if __name__ == "__main__":
   manager = TaskManager()
   manager.add_task("Learn Git", "2024-08-01")
   manager.add_task("Practice OOP", "2024-08-05")
   manager.list_tasks()
   manager.mark_task_completed(1)
   manager.list_tasks()
   # Note: Logic สำหรับ Save/Load ยังไม่ครบถ้วน จะเพิ่มในภายหลังโดยใช้หลักการ Single Responsibility Principle (SRP)
