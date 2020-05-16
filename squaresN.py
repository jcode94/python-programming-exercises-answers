# Question 3
# Level 1

# Question:
# With a given integer n, write a program to generate a dictionary that contains (i, i*i) such that i is an integer
# between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

squarePairs = {}
n = int(input("Enter a number:\n> "))

for i in range(1, n+1):
    d = {i: i * i}
    squarePairs.update(d)

print(squarePairs)

# Solution:
# n=int(raw_input())
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
#
# print d

# Solution just sets each key(i) to the calculation as it creates it. noice
# key to remember just being able to do d[i] = <calculation>
