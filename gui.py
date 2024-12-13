import Functions
import FreeSimpleGUI as sg

label = sg.Text("Enter To-Do:")
input_box = sg.InputText(tooltip="Enter To-Do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=Functions.read_todos(), key="todo_list", enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App", layout=[[label],[input_box, add_button],[list_box],[edit_button]], font=("Helvetica",15))

while True:
    event, value = window.read()
    print(event, value)
    match event:
        case "Add":
            todos_list = Functions.read_todos()
            new_todo = value["todo"]+"\n"
            todos_list.append(new_todo)
            Functions.write_todos(todos_list)
            window["todo_list"].update(values=todos_list)
            window["todo"].update(value="")

        case "Edit":
            selected_todo = value["todo_list"][0]
            todo_to_edit = value["todo"]+"\n"
            #print(todo_to_edit)
            edit_todo_list = Functions.read_todos()
            index = edit_todo_list.index(selected_todo)
            edit_todo_list[index] = todo_to_edit
            Functions.write_todos(edit_todo_list)
            window["todo_list"].update(values=edit_todo_list)
            window["todo"].update(value="")

        case "todo_list":
            selected_todo = value["todo_list"][0]
            window["todo"].update(value=selected_todo)

        case sg.WIN_CLOSED:
            break

window.close()