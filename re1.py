import re
def exam(string):
    pattern='^[a-z]{4}'
    if re.search(pattern,string):
        print("match found")
    else:
        print("not found")
string=input("enter string")
print(exam(string))
        
def my(x):
    x+=[1]
nums=[1,2,3,4]
my(nums)
print(len(nums))


a=100
if(a==100):
    print("correct")
