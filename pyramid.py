#patterns
def pyramid(n):
    k=2*n-3
    for i in range(n): 
        for j in range(k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
n=int(input("enter ur value"))
pyramid(n)



        

            
    
    
