# Question 15
# Level 2
#
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Attempt(didn't get far oof)
# a = int(input('> '))

# Solution:
a = input()
n1 = int(f'{a}')
n2 = int(f'{a}{a}')
n3 = int(f'{a}{a}{a}')
n4 = int(f'{a}{a}{a}{a}')
print(n1 + n2 + n3 + n4)

# Notes: shows the flexibility of string formatting(which i have up to now only used for modifying print
# statements.
