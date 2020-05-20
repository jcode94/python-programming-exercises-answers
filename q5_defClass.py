# Question 5
# Level 1
#
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#
# Hints:
# Use __init__ method to construct some parameters


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
