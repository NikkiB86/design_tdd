def includes_todo():
    todo_list = ["cleaning", "pick up kids", "buy milk"]
    sub = "#TODO"
    return any(sub in list_item for list_item in todo_list)