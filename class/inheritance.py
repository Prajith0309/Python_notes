# [1] single inheritance:
# class dad:
#     def phone(self):
#         print("dad's phone")

# class mom:
#     def mobile(self):
#         print("mom's mobile")


# class son(dad):
#     def use(self):
#         print("son use")

# son1 = son()
# son1.use()
# son1.mobile()
# son1.phone()

# Single Inheritance: This is the most common type of inheritance, where a class inherits from only one parent class. 
# This allows you to reuse methods and attributes from the parent class in the derived class.
#In single inheritance, a class inherits from only one base class.


# [2] multiple inheritance:
# Multiple inheritance allows a class to inherit from more than one base class.
# class dad:
#     def phone(self):
#         print("dad's phone")
# class mom():
#     def mobile(self):
#         print("mom's mobile")


# class son(dad,mom):
#     def use(self):
#         print("son use")

# son1 = son()
# son1.use()
# son1.mobile()
# son1.phone()

# a series ius maintained as chain.


# [3] multilevel inheritance:
# In multilevel inheritance, a class inherits from another class, and then another class inherits from that derived class.
# class Grandparent:
#     pass

# class Parent(Grandparent):
#     pass

# class Child(Parent):
#     pass

# [4] hirarchical inheritance:
# In hierarchical inheritance, multiple classes inherit from a single base class.
# class dad:
#     def phone(self):
#         print("dad's phone")

# class mom(dad):
#     def mobile(self):
#         print("mom's mobile")


# class son(dad):
#     def use(self):
#         print("son use")

# son1 = son()
# mom1 = mom()
# son1.use()
# mom1.phone()
# son1.phone()

# one class to many


# [5] hybrid inheritance:
# Hybrid inheritance is a combination of any two or more types of inheritance mentioned above within a single program.
# when two or more type of inheritance combined together.
# class dad():
#     def money(self):
#         print("dad's money")
    
# class land():
#     def important(self):
#         print("important land")

# class son1(dad,land):
#     pass
# class son2(dad):
#     pass
# class son3(dad):
#     pass

# s2 = son2()
# s2.money()

