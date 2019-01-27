def pat(n):
    num=1
    for i in range(n):
        num = 1 
        for j in range(0,i+1):
            print(num,end=" ")
            num = num + 1
        print("\r")
n=int(input("enter ur rows"))
pat(n)
