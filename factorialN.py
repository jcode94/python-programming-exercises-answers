# Question 2
# Level 1

# Question:
# Write a program which can compute the factorial of a given number.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# My attempt:

while True:
    try:
        num = int(input("Provide a number for which you would like to calculate the factorial.\n> "))
        break
    except ValueError:
        print("Please enter a number.")

output = 1

for i in range(1, num+1):
    output *= i

print(f'{num}! = {output}')

# Sol'n:
# Solution:
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
#
# x=int(input())
# print fact(x)

