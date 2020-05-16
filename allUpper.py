# Question 9
# Level 2
#
# Question:
# Write a program that accepts sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# import sys
# multiline_input = sys.stdin.readlines()
# print(multiline_input)

# Solution:
# lines = []
# while True:
#     s = input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break
#
# for sentence in lines:
#     print(sentence)

# Notes: misunderstood the question as an input block, not consecutive read-ins.

# rewrite for practice

lines = []

while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print(sentence)
