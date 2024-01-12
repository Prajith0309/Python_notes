'''In Python, a context manager is an object that defines the methods __enter__() and __exit__(). 
Context managers are used to set up and tear down resources, such as file operations or network connections, in a clean and controlled way. 
The with statement is commonly used to work with context managers.'''

# Using a Context Manager with the with Statement:
# with context_manager as variable: #--syntax
    # Code block where the resource is used
    # The resource is acquired before entering this block
    # The resource is released when exiting this block

'''The context_manager is the context manager object, and variable is a variable to which the result of __enter__() is assigned.'''

# Example: Using a File as a Context Manager
# Using a file as a context manager to automatically close it
# with open('example.txt', 'r') as file:
#     contents = file.read() # syntax
    # The file is automatically closed when exiting this block

# Code outside the 'with' block; the file is closed at this point
'''In this example, the open() function returns a file object, which acts as a context manager. 
The file is automatically closed when exiting the with block, even if an exception occurs within the block.'''



# custom context managers(not frequently used):
# eg:
class MyContextManager:
    def __enter__(self):
        print("Entering the context")

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            # Exception occurred
            print(f"An exception of type {exc_type} occurred with value: {exc_value}")
        print("Exiting the context")

# Using the custom context manager
with MyContextManager():
    print("Inside the 'with' block")
    # Uncomment the next line to simulate an exception
    # raise ValueError("An example exception")


# eg:2
import time

class TimerContextManager:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Time taken: {elapsed_time} seconds")

# Using the custom context manager
with TimerContextManager() as timer:
    # Code block where timing is measured
    time.sleep(5)
