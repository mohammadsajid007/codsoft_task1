tasks = []

while True:
    print("\n==== To-Do List Menu ====")
    print("1. Add Task")
    print("2. View Task")
    print("3. Exit")

    choice = input("Enter your choice(1-3):")

    if choice == '1':
        new_task = input("Enter the task:")
        tasks.append(new_task)
        print(f"Task'{new_task}' added to the to-do list.")
    elif choice == '2':
        if tasks:
            print("\nYour To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. 1{task}")
        else:
            print("Your to-do list is empty.")
    elif choice == '3':
        print("Exiting the To-Do List application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
