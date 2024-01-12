# types:
# Built-in functions
# User-defined functions
# Lambda functions

# eg:
# built-in func- print(), input(), len() -- these things have functions workings inbulit in python.
# user defined- have a specific structure.
# def add(a,b):
#     return a+b

# addfunc = add(2,3)
# print(addfunc)
# lambda function- can be written in a single line. It is an anonymous function.
# add = lambda x: x * 2
# print(add(2))

# eg:
def add(a,b):
    return a+b

anum = int(input('enter a:'))
bnum = int(input('enter b:'))
func_one = add(anum,bnum)
# print(func_one)
# print(type(func_one))
def mul(one,c):
    return one*c

cnum = int(input('enter c:'))
func_two = mul(func_one,cnum)
print(func_two)

   