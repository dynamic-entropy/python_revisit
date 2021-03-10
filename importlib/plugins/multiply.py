"""
Plugin two - multiplies two numbers
"""


class Plugin:
    def __init__(self, *args, **kargs):
        print("Plugin-two: ", args, kargs)

    def execute(self, a, b):
        print("Multiplying...")
        return a*b
