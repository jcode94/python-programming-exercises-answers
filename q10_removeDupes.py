# Question 10
# Level 2
#
# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing
# all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.

# input_words = input("> ").split(' ')
# parsed = []
#
# for word in input_words:
#     if word not in parsed:
#         parsed.append(word)
#     else:
#         continue
#
# parsed.sort()
# print(' '.join(parsed))

# Solution:
# s = raw_input()
# words = [word for word in s.split(" ")]
# print " ".join(sorted(list(set(words))))

# Notes: set(list) creates a set that only contains the unique values in list.
# Using sorted() over sort() keeps the original list, instead of mutating it as well as works for ANY iterable,
# rather than just lists.

# Revision:
input_words = input('> ').split(' ')
print(' '.join(sorted(set(input_words))))
