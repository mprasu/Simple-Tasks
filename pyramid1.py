def py(n):
    for i in range(n):
        for j in range(i+1):
            print("&",end=" ")
        print("\r")
    
n=int(input("enter ur rows"))
py(n)
