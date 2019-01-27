#multilevel inheritance
class A:
    def show(self):
        print("hello")
class B(A):
    def display(self):
        print("all")
class C(B):
    def view(self):
        print("viewers")

d=C()
d.show()
d.display()
d.view()
