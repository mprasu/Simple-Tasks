class A:
    print("hai")
    x=10#static variable declaration
    def m1(self):
        print("hello")
    #m1()
    def m2(self):
        self.y=20#non-static variable declaration
        self.z=30
        self.t=self.y+self.z
        print(self.t)
A.m1(5)
t1=A()#obj. creation
print(t1)
t1.m1()#v need to pass atleast 1 positional arg.
print(t1.x)#calling static variable outside the class
A.m1("abs")#not creating obj.
t1.m2()
