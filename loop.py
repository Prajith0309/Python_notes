'''for strings:'''

# [1] -- for loop:

# eg-1
# x = "Hello, World!"
# for char in x:
#   print(char)

# eg-2
# vowels = 0
# for char in "Hello, World!":
#   if char in "aeiouAEIOU":
#     vowels += 1

# print(vowels)

# eg-3
# fruits = "apple"
# for i in fruits:
#     print(i)


# [2] -- while loop:

# fruits = "apple"

# index = 0
# while index < len(fruits):
#   print(fruits[index])
#   index += 1

'''for range:'''
# for i in range(start, stop, step):
#   # Statements to be executed for each number in the range

for i in range(1,5,2):
  print(i) #the step value decides which to skip in the sequence

for i in range(1,5,6):
  print(i) #here as the step value is over the range only the start number will be printed.


'''for collections:'''

'''LIST'''
# fruits = ["apple", "banana", "orange"]

# for fruit in fruits:
#   print(fruit)

# numbers = [1, 2, 3, 4, 5]

# count = 0
# for number in numbers:
#   count += 1
#   print(f"inside loop {number}")
# print(f'outside loop {count}')

'''TUPLE'''
# fruits = ("apple", "banana", "orange")

# for fruit in fruits:
#   print(fruit)

# numbers = (1, 2, 3, 4, 5)

# count = 0
# for number in numbers:
#   count += 1

# print(count)

'''SET'''

# fruits = {"apple", "banana", "orange"}

# for fruit in fruits:
#   print(fruit)


# fruits = {"apple", "banana", "orange"}

# fruits.add("grape")

# for fruit in fruits:
#   print(fruit)

# numbers = [1, 2, 3, 4, 5]

# count = 0
# for number in numbers:
#   count += 1

# print(count)

'''DICTIONARY'''

# fruits = {"apple": "red", "banana": "yellow", "orange": "orange"}

# for key in fruits:
#   print(key)


# fruits = {"apple": "red", "banana": "yellow", "orange": "orange"}

# for value in fruits.values():
#   print(value)


# fruits = {"apple": "red", "banana": "yellow", "orange": "orange"}

# for key, value in fruits.items():
#   print(key, ":", value)


'''other loops:'''

'''nested loops'''
# for i in range(3):
#   for j in range(5):
#     print(i, j)

'''Unpacking for loops: 
This type of for loop allows you to unpack a sequence of items into multiple variables simultaneously.'''

for x, y, z in [1, 2, 3]:
  print(x, y, z)





