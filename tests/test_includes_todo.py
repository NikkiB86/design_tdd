from lib.includes_todo import *
import pytest




def test_does_not_include_todo():
    assert includes_todo(["cleaning", "pick up kids", "buy milk"], "#TODO") == False


def test_include_todo():
    assert includes_todo(["cleaning", "pick up kids", "buy milk", "#TODO watch netflix and relax"], "#TODO") == True
