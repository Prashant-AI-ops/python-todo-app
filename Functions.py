def read_todos():
    with open('todo.txt', 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_local):
    with open('todo.txt', 'w') as file_local:
        file_local.writelines(todos_local)
