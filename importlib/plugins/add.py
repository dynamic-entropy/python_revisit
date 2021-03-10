"""
Plugin one - adds two numbers
"""


class Plugin:
    def __init__(self, *args, **kargs):
        print("Plugin-one: ", args, kargs)

    def execute(self, a, b):
        print("Adding...")
        return a+b
