'''Tuples'''

'''
Immutable: 
Tuples are immutable, meaning that their elements cannot be changed after they are created. 
This makes them useful for storing data that should not be modified, such as coordinates or historical records.

Ordered: 
Tuples are ordered, meaning that the order of their elements is preserved when they are accessed. 
This makes them useful for representing sequences of items where the order is important.

Duplicates: 
Tuples allow duplicate elements. 
This means that each element can appear more than once in a tuple.

Purpose: 
Tuples are commonly used to store immutable data, represent fixed sequences, and return multiple values from a function.'''

# Create a tuple containing coordinates
# coordinates = (23.456, 89.123, 89.123)
# print(coordinates)

# Access the first element of the tuple
# x_coordinate = coordinates[0]

# Attempt to change the first element of the tuple (this will result in an error)
# coordinates[0] = 12.345 #TypeError: 'tuple' object does not support item assignment

# coordinates = (23.456, 89.123)  # Create a tuple containing coordinates
# print(coordinates[0])  # Access the first element of the tuple
# print(coordinates[1])  # Access the second element of the tuple
'''In this example, the tuple coordinates represents a set of geographical coordinates. 
The order of the elements in the tuple is important because it determines the order in which the latitude and longitude values are interpreted. 
If the order of the elements were reversed, the coordinates would be interpreted incorrectly.'''


# instructions = ("Preheat oven to 350 degrees F", "Mix dry ingredients", "Combine wet ingredients", "Mix wet and dry ingredients", "Bake for 30 minutes")  # Create a tuple containing baking instructions
# for step in instructions:
#   print(step)  # Print each step of the instructions
'''In this example, the tuple instructions represents a sequence of steps for baking a cake. 
The order of the steps in the tuple is important because it determines the order in which the tasks should be performed. 
If the order of the steps were not preserved, the cake would not be baked correctly.'''

'''Lists'''

'''
Mutable: Lists are mutable, meaning that their elements can be changed after they are created. 
This makes them useful for storing data that may need to be modified, such as shopping lists or to-do lists.

Ordered: 
Lists are ordered, meaning that the order of their elements is preserved when they are accessed. 
This makes them useful for representing sequences of items where the order is important.

Duplicates: 
Lists allow duplicate elements. 
This means that an element can appear multiple times in a list.

Purpose: 
Lists are commonly used to store mutable data, create lists of items, and perform operations on ordered collections.'''

# Create a list containing shopping items
# shopping_list = ["apples", "bananas", "milk", "bread"]

# # Access the second element of the list
# second_item = shopping_list[1]

# # Modify the third element of the list
# shopping_list[2] = "orange juice"

# # Add a new item to the list
# shopping_list.append("eggs")


'''comanality between tuple and list'''
'''It is a best practice to represent sequences of items using ordered data structures like tuples or lists 
when the order of the elements is important. This ensures that the order of the elements is preserved and that the data is interpreted correctly.

Tuples and lists are both ordered collections of items, but they differ in their mutability. 
Tuples are immutable, meaning that their elements cannot be changed after they are created. 
Lists are mutable, meaning that their elements can be changed after they are created.

In situations where the order of the elements is important and the elements need to remain unchanged, tuples are the preferred choice. 
This helps prevent unintended modifications to the data and ensures that the order remains consistent.

For instance, if you're representing a sequence of instructions or a set of coordinates, using a tuple would be appropriate. 
The immutability of tuples ensures that the order of the instructions or coordinates is preserved and that the data is interpreted correctly.

On the other hand, if you have a sequence of items that may need to be modified or updated, a list would be more suitable. 
The mutability of lists allows you to add, remove, or modify elements as needed.'''

'''Sets --- cannot be modified, can only be added or removed.'''
'''
Mutable: 
Sets are mutable, meaning that their elements can be changed after they are created. 
However, unlike lists, sets do not allow duplicate elements.

Unordered: 
Sets are unordered, meaning that the order of their elements is not preserved when they are accessed. 
This makes them useful for representing collections of unique elements where the order is not important.

No duplicates: 
Sets do not allow duplicate elements. 
This means that an element can only appear once in a set.

Purpose: 
Sets are commonly used to store unique elements, perform operations on unordered collections, and eliminate duplicate values.
'''

# # Create a set containing unique numbers
unique_numbers = {1, 2, 3, 4, 5}
print(len(unique_numbers))
unique_numbers[0] = 0 #TypeError: 'set' object does not support item assignment
print(unique_numbers)

# unique_numbers = {1, 2, 3, 4, 5, 5, 5, 4, 3, 2} # even if you add duplicates it wont give error, 
# # at the same time it also wont consider the duplicates.

# # Check if an element exists in the set
# # is_present = 6 in unique_numbers
# # print(is_present)
# # Add a new element to the set
# unique_numbers.add(6)
# print(unique_numbers)
# # Remove an element from the set
# unique_numbers.remove(2)


'''Dictionaries'''

'''Mutable: 
Dictionaries are mutable, meaning that their key-value pairs can be changed after they are created. 
This makes them useful for storing data that may need to be modified, such as user profiles or configuration settings.

Unordered: 
Dictionaries are unordered, meaning that the order of their key-value pairs is not preserved when they are accessed. 
This makes them useful for representing mappings between keys and values where the order is not important.

No duplicates for keys: 
Dictionaries do not allow duplicate keys. This means that each key can only map to one value in a dictionary.

Purpose: 
Dictionaries are commonly used to store key-value pairs, represent mappings between keys and values, and implement lookup tables.'''

# # Create a dictionary containing user information
# user_profile = {'name': 'Alice', 'age': 30, 'age':31, 'city': 'New York'}
# print(user_profile)# even if you add duplicates it wont give error, 
# # at the same time it also wont consider the duplicates.

# Access the value associated with the key 'name'
# user_name = user_profile['name']

# # Modify the value associated with the key 'age'
# user_profile['age'] = 31

# # Add a new key-value pair to the dictionary
# user_profile['occupation'] = 'Software Engineer'

