#polymorphism-doing 1 task in multiple ways/forms
#methodoverriding-same method name and same no. of parameters

class A:
    def show(self):
        print("hello")
class B(A):
    def show(self):
        print("all")
c=B()
c.show() #hello is replaced by all
    
