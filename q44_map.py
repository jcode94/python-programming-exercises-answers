# Question:
# Write a program which can map() to make a list whose elements are square of
# elements in [1,2,3,4,5,6,7,8,9,10].
#
# Hints:
#
# Use map() to generate a list.
# Use lambda to define anonymous functions.

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x ** 2, li))
print(squares)

# Solution:
# li = [1,2,3,4,5,6,7,8,9,10]
# squaredNumbers = map(lambda x: x**2, li)
# print(squaredNumbers)

# Notes: they said to use map to generate a list, yet type(squaredNumbers) == <class 'map'>
# So I think that typecasting it yields the specific result asked for.
