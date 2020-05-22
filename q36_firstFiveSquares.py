# Question:
# Define a function which can generate a list where the values are square of numbers between
# 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
#
# Hints:
#
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list


def firstFive():
    d = [x ** 2 for x in range(1, 21)]
    print(d[:5])


firstFive()

# Solution:
# def printList():
# 	li=list()
# 	for i in range(1,21):
# 		li.append(i**2)
# 	print (li[:5])
#
#
# printList()

# Notes: other than the verbose use of loops by them over listComp, same. Noice. Good slice refresher.