# Question 17
# Level 2
#
# Question:
# Write a program that computes the net amount of a bank account based on a transaction log from console
# input. The transaction log format is shown as following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
netAmount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation == "D":
        netAmount += amount
    elif operation == "W":
        netAmount -= amount
    else:
        pass
print(netAmount)

# Notes: I had net_Total = 0, a while True, an input var, and recognized the need for a dict

# Practice rewrite

net_Total = 0
while True:
    s = input('> ')
    if not s:
        break
    values = s.split(' ')
    operation = [0]
    amount = [1]
    if operation == 'D':
        net_Total += amount
    elif operation == 'W':
        net_Total -= amount
    else:
        pass
print(net_Total)

# Note the step by step parsing of data inputs rather than collection then calculation.
