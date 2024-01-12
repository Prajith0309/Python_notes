import other
print(f"module name of current {__name__}")
val1 = int(input('Enter val1: '))
val2 = int(input('Enter val2: ')) 

#here right after this step the python will see the other module as it is imported and do all the calculations mentioned there,
#so we have to chech fo the current module which is __main__ and then give an if condtionin the module that is imported.

choice = input('Enter your choice: ')

if choice == "+":
    print(other.add(val1,val2))
