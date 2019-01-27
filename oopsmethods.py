#https://youtu.be/qiSCMNBIP2g --->oops concepts link
#https://www.youtube.com/watch?v=qiSCMNBIP2g
#encapsulation---https://www.youtube.com/watch?v=DXJXbJepLP0
#https://www.youtube.com/watch?v=TFLo9m0jFEg
#abstraction--->https://www.youtube.com/watch?v=9ECN--so3hc
#Decorator--->https://www.youtube.com/watch?v=oAz8wz7ClMA
#Generator-->https://www.youtube.com/watch?v=D54x8uSra3Q
class A:
    def __init__(self):# no need of method calling 
        print("hai")
    def config(self):
        print("in config block")
    
a=A()
a.config() #method calling for config block

class B:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print(self.x,self.y)
b=B("hello","world")


class C:
    def __init__(self,x,y):
        self.x=10
        self.y=20
        print(self.x,self.y)
c=C("hello","world")


class D:
    def __init__(self):
        self.x=100 
        self.y=200
d=D()
print(d.x,d.y)

