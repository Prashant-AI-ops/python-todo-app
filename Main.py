from Functions import read_todos, write_todos

prompt = "Todo add/edit/show/finish/exit:"
todo_prompt = "Enter a Task:"

while True:
    user_action = input(prompt)
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = read_todos()
        todos.append(todo+'\n')
        write_todos(todos)

    elif user_action.startswith('show'):
        todos = read_todos()
        for index, items in enumerate(todos):
            items = items.strip('\n')
            row = f"{index+1}-{items}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            choice = int(user_action[5:])
            todos = read_todos()
            print("Editing:", todos[choice - 1].strip('\n'))
            new_todo = input("Enter new Task:") + "\n"
            todos[choice-1] = new_todo
            write_todos(todos)
            print("New Task added")
        except ValueError:
            print("That is not a valid command format.")
            continue

    elif user_action.startswith('finish'):
        try:
            choice = int(user_action[7:])
            todos = read_todos()
            todos.pop(choice-1)
            write_todos(todos)
            print("Todo list has been updated")
        except IndexError:
            print("No such task number exist.")
            continue

    elif user_action.startswith('exit'):
        break
        
    else:
        print("Command is not valid!")
        
print("Bye!")

