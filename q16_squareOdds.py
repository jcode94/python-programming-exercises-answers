# Question 16
# Level 2
#
# Question:
# Use a list comprehension to square(sic, should be 'print') each odd number in a list. The list is input
# by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

userIn = input('> ').split(',')
numbers = [int(x) for x in userIn]
odds = []
for number in numbers:
    if number % 2 != 0:
        odds.append(str(number))
    else:
        pass
print(','.join(odds))

# Note pre solution viewing: This one felt very arbitrary and forced. After a TypeError by not
# doing a str->int list comp conversion early, first solution that came to mind was beating each into type.

# Solution:
# values = raw_input()
# numbers = [x for x in values.split(",") if int(x)%2!=0]
# print ",".join(numbers)

# Notes:
# Wayyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy cleaner. Forgot that you can just
# one-line it all. Still getting used to list comprehensions. They're god-tier. Noting the common practice
# of an initial variable just to hold the user input and then as many as are necessary to modify the input
# as needed. Going to start using the input variable, as it seems to be a 'best practice'.