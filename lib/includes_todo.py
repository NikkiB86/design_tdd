def includes_todo(todo_list, sub):
    return any(sub in list_item for list_item in todo_list)