# Question 14
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case
# letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

input_sentence = list(input('> '))
charType = {'Upper': 0, 'Lower': 0}

for char in input_sentence:
    if char.isupper():
        charType['Upper'] += 1
    elif char.islower():
        charType['Lower'] += 1

print(f'UPPER CASE {charType["Upper"]}')
print(f'LOWER CASE {charType["Lower"]}')

# Solution:
# s = raw_input()
# d={"UPPER CASE":0, "LOWER CASE":0}
# for c in s:
#     if c.isupper():
#         d["UPPER CASE"]+=1
#     elif c.islower():
#         d["LOWER CASE"]+=1
#     else:
#         pass
# print "UPPER CASE", d["UPPER CASE"]
# print "LOWER CASE", d["LOWER CASE"]

# Pretty much identical. However, note the key case matching. Important for clarity.