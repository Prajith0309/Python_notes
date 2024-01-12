'''Iterable in an object which can be iterated, iter() is used to create an iterator object from from an iterable object. 
The next() method is used to iterate through all elemts in the iterable object and it will end when stop execution is triggered.

An iterable is an object that can be iterated over, and an iterator is an object that keeps track of your position in a sequence of data. 
The next() method is used to move forward through the sequence one element at a time, and it will stop when you reach the end of the sequence.'''


# The internal implementation of the iter() function depends on the specific type of iterable object being passed to it. 
# , in general, the iter() function will do the following:

# Check if the object is iterable: 
# The iter() function will first check if the object passed to it is an iterable. 
# If the object is not iterable, the TypeError exception will be raised.

# Create an iterator object: 
# If the object is iterable, the iter() function will create an iterator object from it. 
# The iterator object will keep track of the current position in the sequence of data.

# Return the iterator object: 
# The iter() function will return the iterator object to the caller. 
# The caller can then use the next() method of the iterator to access the next element in the sequence.


'''When you call the iter() function on a list, it creates a new iterator object that is specifically designed to iterate over lists. 
This iterator object keeps track of the current position in the list and provides a next() method for accessing the next element in the list.

So, considering this example, when the iter() is called, it will 1st check if the object is iterable, 
then it will create an iterator object for that iterable and then __iter__() method 
is used to return the iterator object to the caller or in other words, the __iter__() method 
will pass the reference of the iterator object itself to the variable outside in which next() method 
can be used to check the condition if the sequence of data is correct and retrieve one by one, till the condition is not satisfied, 
so that stopiteration() is triggered and it will break the while loop.

The three steps which are done by iter() function is internally managed by __iter__() method.

The __iter__() method is defined within the class of the iterable object. In the case of a list, it's defined within the list class. 
This method is responsible for returning an iterator object for the specific class, allowing you to traverse through the 
elements of the class instance.


The iter() function, on the other hand, is a built-in function in Python that takes an object as an argument and returns an iterator object 
for that object. It internally checks whether the object is iterable and calls the __iter__() method of the object if it is.

In essence, __iter__() is the method that defines how to create an iterator from a specific class, 
while iter() is the function that facilitates iteration over various types of objects, 
including instances of classes that implement the __iter__() method.

So, to answer your question directly, the __iter__() method is indeed inside the iterable object (list, in this case). 
It's like a blueprint for creating an iterator specifically tailored for that object type. 
The iter() function then utilizes this method to obtain the iterator and manage the iteration process.'''


# creating an iterator:
my_list = [1, 2, 3]
my_iterator = iter(my_list)

while True:
    try:
        next_element = my_iterator.next()
        print(next_element)
    except StopIteration:
        break

#internal code:
class list_iterator:
    def __init__(self, list_data):
        self.list_data = list_data
        self.current_index = 0

    def __iter__(self):
        return self

    def next(self):
        if self.current_index < len(self.list_data):
            current_element = self.list_data[self.current_index]
            self.current_index += 1
            return current_element
        else:
            raise StopIteration()
