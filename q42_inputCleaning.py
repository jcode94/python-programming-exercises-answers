# Question:
# Write a program which accepts a string as input to print "Yes" if the string is "yes" or
# "YES" or "Yes", otherwise print "No".
#
# Hints:
#
# Use if statement to judge condition.

s = input('> ')
if s.lower() == 'yes':
    print('Yes')
else:
    print('No')

# Solution:
# s= raw_input()
# if s=="yes" or s=="YES" or s=="Yes":
#     print "Yes"
# else:
#     print "No"

# Notes: Edge case of 'yEs' missed with mine. I should have just gone more specific.

# Rewrite so I don't forget:

# s = input('> ')
# if s == 'yes' or s == 'Yes' or s == 'YES':
#     print('Yes')
# else:
#     print('No')
