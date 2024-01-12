'''
Objects are instances of classes, which are blueprints for creating objects with specific attributes and behaviors. 
Objects encapsulate data and behavior, allowing them to represent real-world entities or concepts. 
Each object has a unique identity and can have attributes that store data specific to that instance. 
Objects can also have methods, which are like functions that define the object's behaviors.

Dictionaries, on the other hand, are specialized data structures designed to store key-value pairs. 
They are collections of unordered pairs where each key uniquely identifies a corresponding value. 
Dictionaries are efficient for accessing values based on their keys, making them well-suited for situations
where data needs to be retrieved quickly based on specific identifiers.
'''

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def greet(self):
#     print(f"Hello, my name is {self.name}.")

# person1 = Person("Alice", 30)
# person1.greet()

# person2 = Person("Bob", 25)
# person2.greet()

# The person1 and person2 objects are instances of the Person class. 
# When these objects are created, the __init__ method is called to initialize their attributes. 
# The greet() method can then be called on these objects to make them say hello.

# In Python, the self keyword refers to the current instance of a class. 
# It is used within methods of a class to access the attributes and methods of that particular instance. 
# The self keyword is essential for object-oriented programming in Python, as it allows you to write code that is both reusable and flexible.

# When you create an object from a class, the class's attributes and methods are copied into the object. 
# However, the self keyword allows you to differentiate between the attributes and methods of the class itself 
# and the attributes and methods of the individual objects that are created from the class.

# Example 1: Accessing class attributes
# class Person:
#   name = "John Doe"  # Class attribute

#   def __init__(self, age):
#     self.age = age  # Instance attribute

# person1 = Person(30)
# person2 = Person(25)

# print(person1.name)  # Output: John Doe (Accessing class attribute)
# print(person2.name)  # Output: John Doe (Accessing class attribute)

# Example 2: Accessing class and instance methods
# class Person:
#     # Define class attribute
#     common_greeting = "Hello from Person class!"

#     def __init__(self, name, age):
#         # Define object attributes
#         self.name = name
#         self.age = age

#     # Access class attribute
#     def greet_class(self):
#         print(f"Class greeting: {Person.common_greeting}")

#     # Access object attribute
#     def greet(self):
#         print(f"Personal greeting: Hello, my name is {self.name} and I am {self.age} years old.")

# # Create an instance of the Person class
# person1 = Person("Alice", 30)
# person1.greet()  # Output: Personal greeting: Hello, my name is Alice and I am 30 years old.
# person1.greet_class()  # Output: Class greeting: Hello from Person class!

# Example 3:
# class Person:
#     def __init__(self, name, age):
#         # Define object attributes
#         self.name = name
#         self.age = age
#     @staticmethod
#     def greet_class():
#         print("Hello from the Person class!")

#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# person1 = Person("Alice", 30)
# person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.
# Person.greet_class()  # Output: Hello from the Person class!


# The self argument needs to be passed to the greet_class() method even though it is not explicitly used within the method. 
# This is because self is a mandatory parameter for all class methods in Python. 
# It is the first argument that is automatically passed to the method when it is called on an instance of the class.

# student_data = {
#   "name": "Alice",
#   "age": 30,
#   "grades": {
#     "math": 90,
#     "science": 85,
#     "english": 95
#   }
# }

# print(student_data["name"])  # Output: Alice
# print(student_data["grades"]["math"])  # Output: 90

# In this example, the student_data dictionary is used to store information about a student. 
# The dictionary has keys that correspond to different pieces of information about the student, such as their name, age, and grades. 
# The values associated with the keys are the actual data for the student.
# It also have a sub-dictionary called 'grades'.


# summary:
# [1] A class must have an __init__ method to define the parameters of the instance to be created.
#     The __init__ method, also known as the constructor, is responsible for initializing the attributes of an object when it is created. 
#     It defines the parameters that are used to set the initial values of the object's attributes.
# [2] All methods of a class must have the self keyword passed as an argument.
#     The self keyword is a mandatory parameter for all class methods in Python. 
#     It refers to the current instance of the class that the method is being called on. 
#     This allows the method to access and modify the attributes and methods of that specific instance.
# [3] If the attribute is from the class,
# then it can be defined inside the class itself or if it comes from the instance then we define it by __init__ method and 
# wherever we use we have to use that with the self keyword.
#     Class attributes are defined directly inside the class body and are shared among all instances of the class.
#     Instance attributes, on the other hand, are defined within the __init__ method and are unique to each instance of the class. 
#     When accessing attributes, you must use the self keyword to refer to instance attributes.
# [4] If a static method is defined inside a function, 
# then we can access that function outside the class by just calling it with the class name and we don't need an instance to access it.
#     Static methods, also known as class methods, are associated with the class itself and do not require an instance of the class to be called. 
#     They are typically used for tasks that are related to the class as a whole rather than to specific instances. 
#     To access a static method, you can call it directly using the class name.