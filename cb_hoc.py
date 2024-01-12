'''A function that is passed as an argument to another function is called a callback function. 
A function that accepts a callback function is called a higher-order function.'''

# positional arguments:
# def greet(name, greeting_function):
#     print(greeting_function(name))

# def hello(name):
#     return f"Hello, {name}!"

# def good_morning(name):
#     return f"Good morning, {name}!"

# greet("Alice", hello)  # Output: Hello, Alice!
# greet("Bob", good_morning)  # Output: Good morning, Bob!



# keyword arguments:
# def hello(name):
#     return f"Hello, {name}!"

# def good_morning(name):
#     return f"Good morning, {name}!"

# def greet(name, greeting_function=hello):
#     print(greeting_function(name))


# greet("Alice")  # Output: Hello, Alice!
# greet("Bob", good_morning)  # Output: Good morning, Bob!


# another example:
# import requests

# def make_request(url, callback):
#     response = requests.get(url)
#     callback(response)

# def print_response(response):
#     print(response.text)

# make_request("https://www.example.com", print_response)
