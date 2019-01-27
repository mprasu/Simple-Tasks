#for finding prime numbers
#l=int(input("enter ur lower bound"))
u=int(input("enter ur upper bound"))
for p in range(2, u):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        print(p)
            
#without using count function
x='s'
y='Mississippi'
count=0
for i in y:
    if i==x:
        count+=1
    else:
        continue
print(count)

#
x=5
y=[2,4,5,6,78,4,5]
count=0
for i in y:
    if i==x:
        count+=1
    else:
        continue
print(count)

# checking words starting with specific character or word
str=input("enter your input")
list=str.split(" ")
char_find=input("enter your character to be find")
for i in list:
    if(i.startswith(char_find)==True):
        print(i)
