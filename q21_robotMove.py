# Question 21
# Level 3
#
# Question
# A robot moves in a plane starting from the original point (0,0). The robot can move toward
# UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from
# current position after a sequence of movement and original point. If the distance is a float, then just
# print the nearest integer.
#
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

from math import sqrt

xCoord = 0
yCoord = 0

while True:
    s = input('> ')
    if not s:
        break
    else:
        s = s.split(' ')
        direction = str(s[0])
        distance = int(s[1])
        if direction == 'UP':
            yCoord += distance
        elif direction == 'DOWN':
            yCoord -= distance
        elif direction == 'LEFT':
            xCoord -= distance
        elif direction == 'RIGHT':
            xCoord += distance
        else:
            pass

print(int(sqrt(xCoord**2 + yCoord**2)))

# Solution
# import math
# pos = [0,0]
# while True:
#     s = raw_input()
#     if not s:
#         break
#     movement = s.split(" ")
#     direction = movement[0]
#     steps = int(movement[1])
#     if direction=="UP":
#         pos[0]+=steps
#     elif direction=="DOWN":
#         pos[0]-=steps
#     elif direction=="LEFT":
#         pos[1]-=steps
#     elif direction=="RIGHT":
#         pos[1]+=steps
#     else:
#         pass
#
# print int(round(math.sqrt(pos[1]**2+pos[0]**2)))

# Notes: I'm pleased with how clean this came across. I need to generalize
# the code, more of pos[0] and less of xCoord. Capiche?

