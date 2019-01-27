#writing data into file
#f=open('E:\python\s.txt',"w")
#f.write("python is a high level \n programming language")
f=open('E:\python\s.txt',"r")
print(f.read())
st=f.read(10)
print("read str is:",st)
#to tell current position of file
p=f.tell()
print("current position",p)
p1=f.seek(0,0)
st=f.read(10)
print("read str is:",st)
print("current position",p1)
print(f.read())
#appending data to a file
f=open('E:\python\s.txt',"a")
f.write("\n  hello django ")

#reading line by line
f=open('E:\python\s.txt')
print(f.readline())


f=open('E:\python\s.txt')
y=f.readlines()
print(y[1])
f.close()

f1=open('E:\python\s1.txt')
x=f1.readlines()
print("no of words is :",len(x))
f1.close()


f2=open('E:\python\s1.txt')
x=f2.readlines()
for i in x:
    print(i.capitalize())
f2.close()
