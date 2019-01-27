#https://www.youtube.com/watch?v=oAz8wz7ClMA
def decorator(f):
    def wrap():
        print("i am in wrapper")
        f()
    return wrap()
def simple():
    print("i am in simple")
d=decorator(simple)

##or

def decorator1(f1):
    def wrap1():
        print("i am in wrapper1")
        f1()
    return wrap1()
@decorator1
def simple1():
    print("i am in simple1")

simple1()    
