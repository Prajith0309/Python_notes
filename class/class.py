# Using Built-in Classes:
'''Python provides a variety of built-in classes for creating objects like integers, strings, lists, dictionaries, and sets. 
These classes simplify object creation by providing pre-defined attributes and behaviors.
For example, when you create the integer 10, you are creating an instance of the int class. 
This object has attributes such as its value (10) and methods such as +, -, *, and /.
Similarly, when you create the string "Hello", you are creating an instance of the str class. 
This object has attributes such as its length (5) and methods such as upper(), lower(), and split().
Tuples are also objects in Python. 
They are similar to lists in that they are ordered collections of items, but they are immutable, 
meaning that they cannot be changed after they are created. Tuples are created using parentheses, while lists are created using square brackets.'''

# Create an integer object
# integer_object = 10

# Create a string object
# string_object = "Hello"

# # Create a list object
# list_object = [1, 2, 3, 4, 5]

# # Create a dictionary object
# dictionary_object = {"name": "Alice", "age": 30}

# # Create a set object
# set_object = {1, 2, 3, 4}

# # Create a tuple object
# tuple_object = (1, 2, 3, 4, 5)

# # In Python, everything is an object, even basic data types like integers, strings, and lists. 
# # This means that every piece of data in a Python program is treated as an instance of a class, which defines its attributes and behavior.

'''Numerical Classes:int, float, complex

Text Processing Classes:str, bytes

Collection Classes:list, tuple, set, dict

Date and Time Classes:datetime, timedelta

Error Classes:Exception, TypeError, ValueError'''

# Defining Custom Classes:

# '''Python's object-oriented programming (OOP) paradigm allows you to create custom classes 
# that define the structure and behavior of objects you want to create. 
# A custom class encapsulates attributes and methods that represent the characteristics and actions of an object.'''

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print("Hello, my name is", self.name)

# # Creating an object from the Person class
# person1 = Person("John", 25)

# # Accessing object attributes
# print("Person's name:", person1.name)
# print("Person's age:", person1.age)

# # Calling object methods
# person1.greet()

'''The __init__() method, also known as the constructor, is responsible for initializing the object's attributes when it's created. 
The greet() method is an example of a behavior that the Person object can perform.'''

# types of class variable:
# [1] instance variable- which comes from self or the object instance.
# [2] this is from the class and will be common for all instance of the class.

# types of class method:
# [1] class methods - which are defined inside the class based on the class and won't use any self keyword (since it do not want to access them).
#                     It can be straight away accessed from the class and does noyt need an instance to access.
# [2] instance method - which is also defined inside class but always takes the self as parameter as it manages the behaviour of the instnces.
# [3] static method - neither the both and it can be accessed directly from the class and do not need an instance to access.


class laptop:
    chargertype="C TYPE"

    def __init__(self,price):
        self.brand=""
        self.price=price
    def setPrice(self,newprice):
        self.price=newprice
    def getPrice(self):
        print(self.price)
    @classmethod                # this decorator must be used or else the name of the class must be passed as the argument while calling the below function.
    def changeChargerType(cls): # here cls must be passed within the braces as it will check the class for the variable.
        cls.chargertype="B TYPE"
        print('charger modified')
    @staticmethod                # this decoratoer denotes that the below function is static and it does'nt need to be changed.
    def info():
        value = 4
        print("This is static info",value)


# laptop.info() #static method calling without even creting the instance of the class.

# laptop.changeChargerType() # calling class method.

hp = laptop(30000)

# getting the initial price:
# hp.getPrice()

# getting the price after setting new one.
hp.setPrice(40000)
hp.getPrice()
