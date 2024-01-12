def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def prod(a,b):
    return a*b
def quo(a,b):
    return a/b
def rem(a,b):
    return a%b

# this will run the below code only if the current module is __main__, 
#if it is used in other modules, then it wont be triggered as then this module wont be the __main__
print(f"module name of other {__name__}")
if __name__ == "__main__": 
    val1 = int(input('Enter val1: '))
    val2 = int(input('Enter val2: '))

    print(add(val1,val2))
    print(sub(val1,val2))
    print(prod(val1,val2))
    print(quo(val1,val2))
    print(rem(val1,val2))

