
# Syntax for creating a generator:
# Creating a generator object:

my_generator_object = my_generator(5)

# Iterating over the generated sequence:

for value in my_generator_object:
    print(value)


# internal code:
def my_generator(n):
    for i in range(n):
        yield i * i


'''Generators are similar to for loops in that they both allow you to iterate over a sequence of values. 
, generators offer more flexibility and control over the iteration process.

With a for loop, you iterate over a predefined sequence of values, and the loop automatically stops once it has reached the end of the sequence. 
With a generator, you have more control over the iteration, and you can pause and resume the iteration at any time using the next() method.

Additionally, generators are more memory-efficient than for loops,
as they generate values on demand rather than storing the entire sequence in memory. 
This makes them particularly well-suited for handling large datasets or infinite sequences.'''


'''so, iterators are better than for loop because, iterators have fewer lines of code and also it can be used to iterate aver the sequence of data 
individually, generators are a more efficient than iterators as they generate the values on the go, 
so they don't store the entire sequence in the memory.'''

'''Iterators are suitable for situations where you need to iterate over an existing collection of data. 
 are more concise and straightforward than for loops, and they provide a simple interface for accessing elements one at a time. 
 Additionally, iterators maintain the state of the iteration, allowing you to pause and resume the process.

Generators, on the other hand, are better suited for generating data on the fly or handling infinite sequences. 
They are more efficient in terms of memory usage, as they don't store the entire sequence in memory but rather generate values as needed. 
 makes them particularly useful for processing large datasets or when you need to perform lazy evaluation.'''

