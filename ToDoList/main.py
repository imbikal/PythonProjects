def to_do_list():
    tasks = []
    print("Simple To-Do List!")
    
    while True:
        print("\nOptions: add, view, remove, quit")
        choice = input("What do you want to do? ").lower()
        
        if choice == "add":
            task = input("Enter a task: ")
            tasks.append(task)
            print("Task added!")
        elif choice == "view":
            print("Your tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        elif choice == "remove":
            task_number = int(input("Enter the task number to remove: "))
            if 0 < task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number.")
        elif choice == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


to_do_list()
