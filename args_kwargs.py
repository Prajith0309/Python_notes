# argument and keyword-arguments

# def demo(*args):
#     for i in args:
#         print(i)

# demo(10,20,35,34)


# def demo(*args):
#     val = 0
#     i=0
#     while i<len(args):
#         val = val+args[i]
#         i = i+1
#     return val
    


# outsideval = demo(10,20,35,34)
# print(outsideval)


def demo(**kwargs):
    for i,j in kwargs.items():
        print(j)

demo(a=10,b=20,c=35,d=34)