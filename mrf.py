'''map(), reduce(), and filter() are built-in functions in Python that operate on iterables. 
They provide a concise and functional programming style for processing and transforming data.'''

# map() Function:
# The map() function applies a given function to all items in an iterable and returns an iterator that produces the results. 
# The syntax is as follows:

# map_result = map(function, iterable)
'''
function: The function to apply to each element of the iterable.
iterable: The iterable (e.g., list, tuple) whose elements will be processed.'''

#  Doubling Values in a List:

numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x: x * 2, numbers)
print(list(doubled_numbers))
# Output: [2, 4, 6, 8, 10]

# reduce() Function:
# The reduce() function from the functools module successively applies a function to the items of an iterable, 
# reducing them to a single cumulative result. 
# The syntax is as follows:

# from functools import reduce

# reduce_result = reduce(function, iterable, [initializer])

'''function: The function to apply cumulatively to the items of the iterable.
iterable: The iterable whose items will be processed.
initializer (optional): An initial value for the accumulation. If not provided, the first two items of the iterable are used.'''

#  Summing Values in a List:

from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)
# Output: 15


# filter() Function:
# The filter() function constructs an iterator from elements of an iterable for which a function returns true. The syntax is as follows:

# filter_result = filter(function, iterable)

'''function: The function that tests whether each element of the iterable is true or false.
iterable: The iterable whose elements will be tested.'''

# Filtering Odd Numbers in a List:

numbers = [1, 2, 3, 4, 5]
filtered_numbers = filter(lambda x: x % 2 == 1, numbers)
print(list(filtered_numbers))
# Output: [1, 3, 5]


# Both map() and filter() functions in Python return iterable objects. 

numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x: x * 2, numbers)
print(doubled_numbers)
# Output: <map object at 0x...>

doubled_numbers_list = list(doubled_numbers)
print(doubled_numbers_list)
# Output: [2, 4, 6, 8, 10]


numbers = [1, 2, 3, 4, 5]
filtered_numbers = filter(lambda x: x % 2 == 1, numbers)
print(filtered_numbers)
# Output: <filter object at 0x...>

filtered_numbers_list = list(filtered_numbers)
print(filtered_numbers_list)
# Output: [1, 3, 5]

# Both map() and filter() objects are iterators, and you can use the next() function to retrieve elements from them one by one.

numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x: x * 2, numbers)

# Using next() to get elements one by one
print(next(doubled_numbers))  # Output: 2
print(next(doubled_numbers))  # Output: 4
print(next(doubled_numbers))  # Output: 6


numbers = [1, 2, 3, 4, 5]
filtered_numbers = filter(lambda x: x % 2 == 1, numbers)

# Using next() to get elements one by one
print(next(filtered_numbers))  # Output: 1
print(next(filtered_numbers))  # Output: 3
print(next(filtered_numbers))  # Output: 5


