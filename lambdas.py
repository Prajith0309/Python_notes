'''In Python, a lambda function is a small anonymous function defined using the lambda keyword. Lambda functions are often used for short, 
simple operations where a full function definition would be overly verbose.'''

# syntax:
# lambda arguments: expression

# eg:
# square = lambda x: x ** 2
# print(square(5))  # Output: 25

'''Lambda functions can take any number of arguments, but the expression must be a single line. 
They are often used in situations where a function is required for a short period and doesn't need a formal name.'''

'''Map, Filter, and Reduce:
Lambda functions are frequently used with functions like map(), filter(), and reduce().'''
# import functools
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(squared_numbers)
# print(even_numbers)

# sum_all = functools.reduce(lambda x, y: x + y, numbers)
# print(sum_all)

'''Sorting:
Lambda functions can be used as the key argument in sorting functions to define custom sorting criteria.'''

pairs = [(1, 5), (2, 3), (4, 1), (3, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)

# In Python, the sorted() function is called with the iterable first, and then additional arguments such as key or reverse are provided.

'''Initialization:

pairs is a list of tuples, where each tuple represents a pair of values.
In this case: [(1, 5), (2, 3), (4, 1), (3, 2)]

Sorting with sorted():

The sorted() function is used to sort the list of tuples (pairs).
The key parameter is provided, which is a function to extract a comparison key for each element. 
In this case, the lambda function lambda x: x[1] is used.

Lambda function as the key:

The lambda function takes an argument x (which represents each tuple in the list).
x[1] extracts the second element of the tuple (index 1), which is the basis for sorting.

Sorting Criteria:

The sorted() function uses the values returned by the lambda function (x[1]) as the sorting key.
The list is sorted in ascending order based on the second element of each tuple.

Result:

The sorted result is assigned to the variable sorted_pairs.'''


'''GUI applications:
Lambda functions are useful in GUI programming, particularly for defining event handlers.'''

# button = Button(root, text="Click me", command=lambda: print("Button clicked")) # will work only in browser


'''Functional programming:
Lambda functions are often used in functional programming paradigms, where functions can be passed as arguments to other functions.'''

# def apply_operation(x, y, operation):
#     return operation(x, y)

# add = lambda x, y: x + y
# result = apply_operation(3, 4, add)
# print(result)
