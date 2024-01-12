'''In Python, decorators are a powerful and flexible way to modify or extend the behavior of functions or methods 
without changing their actual code. Decorators use the @decorator syntax and are applied to functions or methods to wrap or modify their behavior. 
They are commonly used for tasks like logging, timing, access control, and more.'''

# syntax:
# @decorator
# def my_function():
#     # function code


# eg:1
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!") #This is equivalent to say_hello = my_decorator(say_hello). The my_decorator function is called with say_hello as an argument, and it returns the wrapper function.

say_hello()#When you call say_hello(), you're actually calling the wrapper function returned by the decorator. The wrapper function contains the logic to execute before and after the original function call.

'''The execution of the wrapper function actually happens when you call the decorated function (say_hello in this case).
Execution Flow:

The wrapper function is executed.
It prints "Something is happening before the function is called."
It calls the original function (func()), which is the original say_hello function.
The original function prints "Hello!"
The wrapper function prints "Something is happening after the function is called."'''
