# Question:
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in
# one line and the last half values in one line.
#
# Hints:
#
# Use [n1:n2] notation to get a slice from a tuple.

tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tp[:int((len(tp) + 1) / 2)])
print(tp[int((len(tp) + 1) / 2):])

# Solution:
# tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# tp1 = tp[:5]
# tp2 = tp[5:]
# print(tp1)
# print(tp2)

# Notes: Not sure where to draw the line with separation of steps.
# Mine is more generalized but if tuple length is static and known, ezclap.
