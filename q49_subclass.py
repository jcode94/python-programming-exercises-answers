# Question:
# Define a class named American and its subclass NewYorker.
#
# Hints:
#
# Use class Subclass(ParentClass) to define a subclass.


class American(object):
    pass


class NewYorker(American):
    pass


anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)
print(aNewYorker)

# Solution
# class American(object):
#     pass
#
# class NewYorker(American):
#     pass
#
# anAmerican = American()
# aNewYorker = NewYorker()
# print anAmerican
# print aNewYorker

# Notes: This one I actually got! I am pretty sure I understand how the parent-child relationship works
# in terms of python class attribute sharing, at least in terms of nomenclature.
