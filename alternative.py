#Replacing Odd and Even-indexed characters in a string in Python
s=input("enter your string:")
s1=" "
x=s[::-1]
index=0
for c in x:
    if(index%2==0):
        s1+=c.upper()
    else:
        s1+=c.lower()
    index+=1
print(s1)



