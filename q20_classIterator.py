# Question 20
# Level 3
#
# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7,
# and between a given range 0 and n.
#
# Hints:
# Consider use yield

# Solution: (have to start mentally breaking them down. They're much simpler than I'm making them out to be.


def div7(r):
    i = 0
    while i < r:
        j = i
        i += 1
        if j % 7 == 0:
            yield j

