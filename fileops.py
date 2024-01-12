

Opening a File:
# Open a file in read mode
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)



Reading from a File:
# Read the entire content of a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
    
# Read line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line)




Writing to a File:
# Open a file in write mode
with open('output.txt', 'w') as file:
    file.write("This is a sample text.\n")
    file.write("Another line.")




Appending to a File:
# Open a file in append mode
with open('output.txt', 'a') as file:
    file.write("Appending a new line.\n")



Deleting a File:
import os

# Delete a file
file_path = 'output.txt'
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print("File does not exist.")




Clearing a File (Truncate):
# Open a file in write mode and truncate its content
with open('output.txt', 'w') as file:
    file.truncate()
