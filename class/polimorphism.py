# Polymorphism and inheritance are both fundamental concepts in object-oriented programming (OOP) 
# that play crucial roles in designing flexible and reusable code. 
# While they are interrelated, they serve distinct purposes and exhibit different characteristics.

# Inheritance is the mechanism by which a class inherits the properties and methods of another class, 
# establishing a hierarchical relationship between them. The inheriting class, known as the subclass, 
# gains access to the features of the parent class, called the superclass. This allows for 
# code reuse and promotes the organization of classes based on their similarities and specialization.

# Polymorphism, on the other hand, refers to the ability of objects to take on many forms. 
# It enables a single method or operator to have different implementations based on the type of object it interacts with. 
# This flexibility promotes loose coupling and enhances code adaptability.

'''
Both concepts are closely tied to object-oriented programming principles.
They contribute to the creation of well-structured and maintainable code.
They enhance the flexibility and adaptability of code.
'''

'''
Inheritance establishes a parent-child relationship between classes, while polymorphism deals with the behavior of methods and operators.
Inheritance operates at the class level, while polymorphism primarily functions at the method level.
Inheritance is primarily used for code reuse and organization, while polymorphism focuses on adapting code to different object types.
Inheritance is typically determined at compile time, while polymorphism can be determined at both compile time and run time.
Inheritance exhibits different forms, such as single, multiple, hierarchical, and multilevel, while polymorphism manifests as overloading and overriding.
'''

# There are two main types of polymorphism in Python: compile-time (or static) polymorphism and runtime (or dynamic) polymorphism.

'''Compile-time Polymorphism:

Also known as method overloading or operator overloading.
It occurs when the same method or operator is defined multiple times in the same class with different parameters.
Python does not support traditional method overloading, 
but you can achieve a form of it using default parameter values and variable-length argument lists.'''

# eg:1
# class MathOperations:
#     def add(self, a, b=None, c=None):
#         if b is not None and c is not None:
#             return a + b + c
#         elif b is not None:
#             return a + b
#         else:
#             return a

# math_obj = MathOperations()
# print(math_obj.add(2))           # Output: 2
# print(math_obj.add(2, 3))        # Output: 5
# print(math_obj.add(2, 3, 4))     # Output: 9


# eg:2
# class MathOperations:
#     def add(self, a, b):
#         return a + b

#     def add_three(self, a, b, c):
#         return a + b + c

# # Creating an instance of MathOperations
# math_obj = MathOperations()

# # Calling different methods based on the number of arguments
# print(math_obj.add(2, 3))          # Output: 5
# print(math_obj.add_three(2, 3, 4))  # Output: 9


'''Runtime Polymorphism:

Also known as method overriding or dynamic polymorphism.
It occurs when a method in a child class has the same name and signature as a method in its parent class.
The actual method that gets called is determined at runtime based on the type of object.'''

# eg:
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# def animal_sound(animal_obj):
#     return animal_obj.speak()

dog_obj = Dog()
cat_obj = Cat()

'''Function Parameter Polymorphism (also Run-time Polymorphism):

In the second example, you define a function animal_sound that takes an animal_obj parameter. The function expects animal_obj to be an object of a class that inherits from Animal and has a speak method.
Polymorphism is achieved when you call animal_sound with instances of both Dog and Cat. The function indirectly calls the speak method on the provided object.
This is another example of run-time polymorphism, but it's achieved through a function parameter.'''
# print(animal_sound(dog_obj))  # Output: Woof!
# print(animal_sound(cat_obj))  # Output: Meow!


'''Method Overriding (Run-time Polymorphism):

In the first example, you have a base class Animal with a method speak, and two derived classes Dog and Cat that override the speak method with their own implementations.
Polymorphism is achieved at runtime when you create instances of Dog and Cat and call their speak methods. The specific implementation of speak is determined by the actual type of the object at runtime.
This is an example of run-time polymorphism or method overriding.'''
print(dog_obj.speak())  # Output: Woof!
print(cat_obj.speak())  # Output: Meow!
