class A:
    def show(self):
        print("hello")

class B:
    def display(self):
        print("all")
class C(A,B):
    def view(self):
        print("viewers")

d=C()
d.show()
d.display()
d.view()
