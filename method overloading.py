#methodoverloading-same method name and diff no. of parameters

class A:
    def show(self,a,b):
        return a+b

    def show(self,a,b,c):
        return a+b+c

c=A()
print(c.show(2,3,1))
print(c.show(2,3)) #python doesn't support this
