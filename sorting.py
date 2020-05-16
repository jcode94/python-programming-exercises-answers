# Question 8
# Level 2
#
# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a
# comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# 1st Attempt:
# input_string = input("> ").split(',')
#
# input_string.sort()
# print(input_string)

# Solution:
# items=[x for x in raw_input().split(',')]
# items.sort()
# print ','.join(items)

# Notes: Whoops, I forgot to check output format. Also, let's start using this list comprehension thingy.


# Amended:
input_string = [x for x in input().split(',')]
input_string.sort()
print(','.join(input_string))
