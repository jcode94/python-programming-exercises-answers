# Question 25
# Level 1
#
# Question:
#     Define a class, which have a class parameter and have a same instance parameter.
#
# Hints:
#     Define a instance parameter, need add it in __init__ method
#     You can init a object with construct parameter or set the value later

# No idea how to do this so this will be a learning experience. With 80+ exercises left, I think it won't be remiss.

# Solution:


class Person:
    # Define the class parameter "name"
    name = "Person"

    def __init__(self, name=None):
        # self.name is the instance parameter
        self.name = name


jeffrey = Person("Jeffrey")
print(f'{Person.name} name is {jeffrey.name}')

nico = Person()
nico.name = "Nico"
print(f'{Person.name} name is {nico.name}')

# I think I get it?
