def msg():
    print("hai")
msg()
msg()

def add(a,b):#non-default parameters
    return a+b
print(add(2,3))

def add1(a=1,b=5):#default parameters
    print(a+b)
add1()

def sub(a,b):
    print(a-b)
sub(5,2)

def sub(a,b):
    return a-b
sub(5,2)#no o/p becoz there is no return stmt

def sub(a=9,b=2):
    print(a-b)
sub(5,2)

def f(*x):#arbituary arguments
    print(x)
    print(type(x))
f(4,'app',4+3j,7.4,1)

def f(**x):#kwargs
    print(x)
    print(type(x))
f(name='abs',age=29)

y=10#global variable
def f1():
    print(y)
f1()

def f1():
    y=20#local variable
    print(y)
f1()

