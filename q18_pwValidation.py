# Question 18
# Level 3
#
# Question:
# A website requires the users to input username and password to register. Write a program to check the
# validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to
# the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Attempt
# pw_inputs = input('> ')
# pws = pw_inputs.split(',')
# valid_pws = []
# sym_options = ['$', '#', '@']
# for pw in pws:
#     charPW = list(pw)
#     reqs = {'lower': 0, 'num': 0, 'upper': 0, 'sym': 0, 'len': 0}
#     for char in charPW:
#         if char.islower() and reqs['lower'] == 0:
#             reqs['lower'] += 1
#         elif char.isdigit() and reqs['num'] == 0:
#             reqs['num'] += 1
#         elif char.isupper() and reqs['upper'] == 0:
#             reqs['upper'] += 1
#         elif str(char) in sym_options and reqs['sym'] == 0:
#             reqs['sym'] += 1
#         else:
#             pass
#     if 0 in reqs.values():
#         pass
#     else:
#         valid_pws.append(pw)
# print(','.join(valid_pws))

# Solutions:
# import re
# value = []
# items=[x for x in raw_input().split(',')]
# for p in items:
#     if len(p)<6 or len(p)>12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]",p):
#         continue
#     elif not re.search("[0-9]",p):
#         continue
#     elif not re.search("[A-Z]",p):
#         continue
#     elif not re.search("[$#@]",p):
#         continue
#     elif re.search("\s",p):
#         continue
#     else:
#         pass
#     value.append(p)
# print ",".join(value)

# Notes: very cool use of both the gating nature of loops/code blocks and the re module and search function
# Also, note that the first check was for length, a top level analytic versus a by-character check
# Rewrite for practice

import re
value = []
items = [x for x in input('> ').split(',')]
for p in items:
    if len(p) < 6 or len(p) > 12:
        continue
    else:
        pass
    if not re.search('[a-z]', p):
        continue
    elif not re.search('[0-9]', p):
        continue
    elif not re.search('[A-Z]', p):
        continue
    elif not re.search('[$#@]', p):
        continue
    elif re.search('\s', p):
        continue
    else:
        pass
    value.append(p)

print(','.join(value))
