'''The super() function in Python is used to call a method from a parent class. 
It is commonly used in the context of inheritance to invoke the method of the parent class. 
Here are some examples to illustrate the use of super():'''


# class a():
#     def __init__(self):
#         print("A")
#     def display(self):
#         print("you are in class A")


# class b():
#     def __init__(self):
#         print("B")
#     def display(self):
#         print("you are in class B")


# class c(b,a):
#     def __init__(self):
#         super().__init__()
#         print("C")
#     def display(self):
#         print("you are in class C")

# obj= c()

#  super keyword will help access the constructor of other class and hence inheritance is more effective.
#  if two or more classes is inherited in a single class, then the left most one will work with the super keyword.
#  if the left most one have a super keyword  used, then it will be considering the next parameter as passesd with it as the parent.
# if the left most one have a super keyword  used, then it will be considering the next parameter as passesd with it as the parent, 
# but if there is no parameter after that, the super function will consider its parent class which is passed inside like eg: childclass(parentclass)
# eg:
# class a():
#     def __init__(self):
#         print("A")
#     def display(self):
#         print("you are in class A")


# class b():
#     def __init__(self):
#         super().__init__()
#         print("B")
#     def display(self):
#         print("you are in class B")


# class c(b,a):
#     def __init__(self):
#         super().__init__()
#         print("C")
#     def display(self):
#         print("you are in class C")

# obj= c()

# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print("Parent class:", self.name)

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)  # Calling the __init__ method of the parent class
#         self.age = age

#     def display(self):
#         super().display()  # Calling the display method of the parent class
#         print("Child class:", self.age)

# # Creating an instance of the Child class
# child_obj = Child("Alice", 10)

# # Calling the display method of the Child class
# child_obj.display()


class A:

    # ---eg:*
    # def method1(self):
    #     print("Class A")


    def method(self):
        print("Class A")

class B(A):
    def method(self):
        print("Class B")

        # ---eg:*
        # method1() 

        super().method()

class C(A):
    def method(self):
        print("Class C")
        super().method()

class D(B,C):
    def method(self):
        print("Class D")
        super().method()

# Creating an instance of the D class
d_obj = D()

# Calling the method of the D class
d_obj.method()

# clarification:
# ----this is regarding the confusion of acsessing the method of other class outside the child class and inside the class---- denotet by eg:*
# (consider only the A parent and B(A) child classes)
# when inheritance is used and the method of the parent class in accessed from the instance of child class super function is not needed
# when the method of the parent class need to be used inside the child class or inside a method of theb child class we need to use super function
# b_obj = B()
# b_obj.method()

