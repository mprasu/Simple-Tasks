def py(n):
    for i in range(n):
        for j in range(n-1-i):
            print(" ",end=" ")
        for z in range(0,2*i+1):
            print("#",end=" ")
        print("\r")
n=int(input("enter ur value:"))
py(n)
