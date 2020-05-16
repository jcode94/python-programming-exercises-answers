# class InputOutString(object): # name obviously taken from solution, this one was out of my base
#     def __init__(self):
#         self.string = ""
#
#     def getString(self):
#         self.string = str(input("Enter a string:\n> "))
#
#     def printString(self):
#         print(self.string.upper())


# Solution:

class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("> ")

    def printString(self):
        print(self.s.upper())


strObj = InputOutString()  # This part makes the instance that takes control of the methods available
strObj.getString()
strObj.printString()
