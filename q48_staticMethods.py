# Question:
# Define a class named American which has a static method called printNationality.
#
# Hints:
#
# Use @staticmethod decorator to define class static method.

#
# class American:
#     @staticmethod
#     def printNationality(self):
#         self.nationality = "American"

# Imma be honest, I have no idea how to do this, even after googling.

# Solution:


# class American(object):
#     @staticmethod
#     def printNationality():
#         print("America")
#
#
# anAmerican = American()
# anAmerican.printNationality()
# American.printNationality()

# Rewrite for practice:


class American(object):
    @staticmethod
    def printNationality():
        print("America")


anAmerican = American()
anAmerican.printNationality()
American.printNationality()

# ln 38 creates an instance but lines 39 and 40 show that regardless of the instance the staticmethod
# yields the same output.