def printMissing(arr, n, low, high): 
  
    # Insert all elements of  
    # arr[] in set  
    s = set(arr) 
  
    # Traverse through the range  
    # and print all missing elements  
    for x in range(low, high + 1): 
        if x not in s: 
            print(x, end = ' ') 
  
# Driver Code  
arr = [1, 3, 5, 44,34] 
n = len(arr) 
low, high = 1, 50
printMissing(arr, n, low, high) 
