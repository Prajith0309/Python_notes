# error in python:
'''
  syntax error - if structure is wrong.

  name error - if the identifier is not recognized within the current scope
  Name errors arise when the code attempts to access a variable or function that hasn't been defined yet.

  type error - This happens when you try to perform an arithmetic operation on a string, for instance, 
  or when you assign a value of the wrong type to a variable.

  value error - ValueErrors occur when an operation is attempted with an invalid or inappropriate value.

  index error - Index errors occur when you try to access an element in a sequence using an invalid index.

  key error - Key errors occur when you try to access a key in a dictionary that doesn't exist.

  attribute error -  A class is a blueprint for creating objects. Objects are instances of a class, 
  and they have attributes that store data. Attributes are like variables that belong to an object. 
  For example, a class called Person might have attributes like name, age, and address.
  A dictionary is a collection of key-value pairs. Keys are used to identify the values in a dictionary. 
  For example, a dictionary of student names and grades might have keys like "Alice", "Bob", and "Charlie". 
  The values associated with these keys would be the students' grades.
  Attribute errors occur when you try to access an attribute or method of an object that doesn't exist.

  runtime error - Runtime errors occur during the execution of the program, not during the compilation phase. 
  These errors are caused by logical mistakes in the code, such as infinite loops, incorrect conditional statements, or invalid memory access. 
  Runtime errors can halt the program's execution abruptly.

  import error - Import errors occur when the code attempts to import a module that doesn't exist or when the module path is incorrect.

  oserror/filenotfounderror - OSError refers to errors related to the operating system, such as file I/O issues or permission-related problems. 
  These errors occur when the program interacts with the operating system and encounters issues like file not found, 
  permission denied, or invalid file structure.
'''
# # syntax error:
# print 10 + 5

# # name error:
# print(x)

# type error:
# print(10 + "hello")

# # value error:
# string_value = "hello"
# integer_value = int(string_value)
# print(type(integer_value))

# # index error:
# my_list = [1, 2, 3]
# print(my_list[3])

# # key error:
# my_dict = {"a": 1, "b": 2, "c": 3}
# print(my_dict["d"])


# # attribute error:
# class MyObject:
#   pass

# my_object = MyObject()
# print(my_object.x)

# runtime error:
# example are while loop without correct ending statement as it can create infinite loop

# # import error:(if path is wrong) && ModuleNotFoundError:(if module name is not found)
# import my_module

# # filenotfounderror:
# open("myfile.txt", "r")
