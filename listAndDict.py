# Question 4
# Level 1
#
# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generates a list and
# a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


n = input("> ").split(',')
print(list(n))
print(tuple(n))

# Solution:
# values=raw_input()
# l=values.split(",")
# t=tuple(l)
# print l
# print t

# Note the separation of input and parsing the input. This appears to be a 'best practice' method
# and less so a logical step.

