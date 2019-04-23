"""
This module is a foolish module that take some data and passes it around the 
application
"""


value = 100


def picker(parameter):
    print(parameter)
    global value
    value = parameter


def setter():
    global value
    return value
