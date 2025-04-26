task_list = []

while True:
    print("     MENU")
    print("----------------")
    print("a) Add a task")
    print("b) View tasks")
    print("c) End the program\n")
    while True:
        user_choice = input("Your choice (a, b, c): ")
        if user_choice not in ["a", "b", "c"]:
            print("Wrong letter!. Try again\n")
        else:
            break
    
    if user_choice == "a":
        new_task = input("Write a new task: ")
        task_list.append(new_task)
        print("Task was added to a list.")
        continue
    elif user_choice == "b":
        if len(task_list) == 0:
            print("No tasks.")
        else:
            for index, task in enumerate(task_list, start = 1):
                print(index, task)
            continue
    elif user_choice == "c":
        print("End of a program. See you later!")
        break