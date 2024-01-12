'''A dictionary comprehension is a concise and expressive way to create dictionaries in Python. 
It allows you to construct a new dictionary by specifying both the key and the corresponding value using an expression, 
similar to a list comprehension.'''

# Dictionary Comprehension Syntax:
# new_dict = {key_expression: value_expression for item in iterable if condition}

'''key_expression: The expression to compute the key for each item.
value_expression: The expression to compute the value for each item.
item: The variable representing each element in the iterable.
iterable: The sequence or iterable you are iterating over.
condition (optional): An optional condition that filters the items based on a specified criterion.'''

# Dictionary Comprehension Examples:

# Creating a Dictionary from Two Lists:
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}
print(my_dict)
'''This creates a dictionary my_dict with keys from the keys list and corresponding values from the values list.'''

# Squaring Values in a Dictionary/Data Transformation::
original_dict = {'a': 2, 'b': 3, 'c': 4}
squared_dict = {k: v**2 for k, v in original_dict.items()}
print(squared_dict)

# Filtering Items in a Dictionary:
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = {k: v for k, v in original_dict.items() if v > 2}
print(filtered_dict)

# Combining Multiple Dictionaries:
keys1 = ['a', 'b', 'c']
values1 = [1, 2, 3]

keys2 = ['d', 'e', 'f']
values2 = [4, 5, 6]

combined_dict = {k: v for k, v in zip(keys1, values1)}
combined_dict.update({k: v for k, v in zip(keys2, values2)})
print(combined_dict)

# Dynamic Key-Value Generation:
base_number = 10
dynamic_dict = {f'key_{i}': base_number + i for i in range(5)}
print(dynamic_dict)

# Mapping Keys to Values:
original_dict = {'apple': 'fruit', 'carrot': 'vegetable', 'banana': 'fruit'}
mapped_dict = {key.capitalize(): value for key, value in original_dict.items()}
print(mapped_dict)


