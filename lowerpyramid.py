def pa(n):
    for i in range(n):
        for j in range(0,i):
            print(end=" ")
        for z in range(n-i):
            print("* ",end=" ")
        print("\r")
n=int(input("enter ur value"))
pa(n)
