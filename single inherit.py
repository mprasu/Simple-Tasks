#single inheritance
class A:#class definition
    def show(self):
        print("hai")
class B(A):
    def display(self):
        print("world")
a=B() #object creation
a.show()#method calling
a.display()
    
