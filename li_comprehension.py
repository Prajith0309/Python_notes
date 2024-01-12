'''List comprehension is a concise and expressive way to create lists in Python. 
It provides a more compact syntax for generating lists compared to traditional methods involving loops and explicit append statements. List comprehensions allow you to create a new list by applying an expression to each item in an existing iterable (e.g., a list, tuple, or range) 
and optionally filtering the items based on a condition.'''

# syntax:
# new_list = [expression for item in iterable if condition]

'''
expression: The value to be included in the new list.
item: The variable representing each element in the iterable.
iterable: The sequence or iterable you are iterating over (e.g., a list, tuple, or range).
condition (optional): An optional condition that filters the elements based on a specified criterion.
'''

# List Comprehension Example:

squares_of_evens = [x**2 for x in range(10) if x % 2 == 0]
print(squares_of_evens)

# Uses of List Comprehension:

'''Filtering Elements:

List comprehensions are often used to create a new list by filtering elements based on certain conditions.'''

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

'''Transforming Elements:

You can use list comprehensions to transform elements of an existing list.'''

squares = [x**2 for x in range(5)]
print(squares)

'''Combining Elements from Multiple Lists:

List comprehensions can be used to combine elements from multiple lists.'''

combined = [(x, y) for x in ['a', 'b', 'c'] for y in [1, 2, 3]]
print(combined)

'''Creating Lists from Iterables:

List comprehensions provide a concise way to create lists from existing iterables.'''

words = ['hello', 'world']
# print(type(words))
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

'''Nested List Comprehensions:

You can use nested list comprehensions to create lists of lists.'''

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [element for row in matrix for element in row]
print(flattened)

