# Question:
# Write a program which can filter even numbers in a list by using filter function.
# The list is: [1,2,3,4,5,6,7,8,9,10].
#
# Hints:
#
# Use filter() to filter some elements in a list.
# Use lambda to define anonymous functions.

ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda x: x % 2 == 0, ten)
print(evens)

# Solution:
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evenNumbers = filter(lambda x: x % 2 == 0, li)
# print(evenNumbers)

# Notes: a little bit of research yielded a not so bad foray into both filter() and lambda functions.
