from lib.includes_todo import *
import pytest




def test_does_not_include_todo():


    assert includes_todo() == False


def test_include_todo():
    includes_todo()
    includes_todo.todo_list.append

    assert includes_todo() == True
