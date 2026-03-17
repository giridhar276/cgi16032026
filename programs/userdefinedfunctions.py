# fixed arguments
def display(a,b):
    print(a,b)
display(10,20)

# default arguments
def display(a = 0,b = 0,c = 0,d = 0):
    print(a,b,c,d)
display()
display(10)
display(10,20)
display(10,20,30)
display(10,20,30,40)

# keyword arguments
def display(c,a,b):
    print(a,b,c)
display(b = 20,c= 30,a =10)

# variable length arguments
def display(*args):   # *args is a tuple
    for val in args:
        print(val)
    print("total sum :",sum(args))
display(10,20,30,40,50,60,70,80,90,100,110,120,13,53,43,54,23,645,2,423)


def displayinfo(**kwargs):
    print(kwargs)
    for k,w in kwargs.items():
        print(k,w)
displayinfo(chap1=10,chap2=30)


