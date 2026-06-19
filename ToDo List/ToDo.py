
while True:

  print("\n====== To Do List ======\n")
  
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Delete Task")
  print("4. Mark Task as Completed")
  print("5. Exit")

  choice = input("Enter your choice: ")

  # Add a Task

  if choice == '1':
    task_name = input("Enter the task: ")

    with open("tasks.txt", "a") as file:
      file.write(task_name + "\n")
      
    print("Task added successfully!")

  # View a Task

  elif choice == '2':
    try:
      with open("tasks.txt", "r") as file:
        tasks = file.readlines()

        if not tasks:
          print("No tasks available at the moment.")

        else:
          print("\nTasks:")
          for index, task in enumerate(tasks, start = 1):
            print(f"{index}. {task.strip()}")

    except FileNotFoundError:
      print("No tasks available at the moment.")

  # Delete a Task
  
  elif choice == '3':
    try:
      with open("tasks.txt", "r") as file:
        tasks = file.readlines()

      if not tasks:
        print("No tasks available to delete.")
      else:
        print("\nTasks:")

        for index, task in enumerate(tasks, start=1):
          print(f"{index}. {task.strip()}")

        task_num = int(input("Enter task number to delete: "))

        if 1 <= task_num <= len(tasks):
          deleted_task = tasks.pop(task_num - 1) 

          with open("tasks.txt", "w") as file:
            file.writelines(tasks)

          print(f"Task '{deleted_task.strip()}' deleted successfully!")

        else:
          print("Invalid task number.")

    except FileNotFoundError:
      print("No tasks available to delete.")
             

  # Mark a Task as Completed

  elif choice == '4':
    try:
      with open("tasks.txt", "r") as file:
        tasks = file.readlines()

      if not tasks:
        print("No tasks available to mark as completed.")
      else:
        print("\nTasks:")

        for index, task in enumerate(tasks, start=1):
          print(f"{index}. {task.strip()}")

        task_num = int(input("Enter task number to mark as completed: "))

        if 1 <= task_num <= len(tasks):
          completed_task = tasks[task_num - 1].strip() + " (Completed)\n"
          tasks[task_num - 1] = completed_task

          with open("tasks.txt", "w") as file:
            file.writelines(tasks)

          print(f"Task '{completed_task.strip()}' marked as completed!")

        else:
          print("Invalid task number.")

    except FileNotFoundError:
      print("No tasks available to mark as completed.")


  # Exit the Program
   
  elif choice == '5':
    print("Exiting the program...")
    break

  else:
    print("Invalid choice. Please try again.")
