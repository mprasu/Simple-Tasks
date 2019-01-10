L1 = ['a', 'b', 'c']
L2 = ['b', 'd']
#converting list to set format
c1=set(L1)
print(c1)
c2=set(L2)
print(c2)
#for common elements
print(c1.intersection(c2))
#elements present in L1 and not in L2
print(c1.difference(c2))

#mad libs
name=input("enter ur name")
age=input("enter ur age")
location=input("enter ur location")
print("hello !"+name)
print("may age is" +age+ "and stays in"+location)
#calculator
a=input("enter a no.")
b=input("enter another no.")
c=float(a)+float(b)
print(c)
d=a+b
print(d)
