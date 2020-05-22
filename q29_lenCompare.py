# Question:
# Define a function that can accept two strings as input and print the string with maximum length
# in console. If two strings have the same length, then the function should print al l strings line
# by line.
#
# Hints:
#
# Use len() function to get the length of a string


def strCompare(a, b):
    if len(a) > len(b):
        print(a)
    elif len(b) > len(a):
        print(b)
    else:
        print(a)
        print(b)


strCompare('hello', 'brittanie')

# Solution:
# def printValue(s1, s2):
#     len1 = len(s1)
#     len2 = len(s2)
#     if len1 > len2:
#         print(s1)
#     elif len2 > len1:
#         print(s2)
#     else:
#         print(s1)
#         print(s2)
#
# printValue("one", "three")

# Notes: Looks pretty fuckin good to me. Only difference is they separated the parameters from the
# variables that the function handles. This may be good for debugging. I'll keep my eyes open for that.
