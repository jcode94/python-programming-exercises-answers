# Question:
# Define a function which can generate and print a tuple where the value are square of
# numbers between 1 and 20 (both included).
#
# Hints:
#
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use tuple() to get a tuple from a list.


def pairToTuple():
    d = [(x, x ** 2) for x in range(1, 21)]
    for x in d:
        print(x)


pairToTuple()

# Solution:
# def printTuple():
# 	li=list()
# 	for i in range(1,21):
# 		li.append(i**2)
# 	print tuple(li)
#
# printTuple()

# Notes: if this was just to learn the tuple typecast, I got it. Otherwise, good practice for tuple-in-list
# comprehension.