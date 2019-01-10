#Basic Calculator
try:
    num1=float(input("enter a number:"))
    num2=float(input("enter another number:"))
    op=input("enter your operation:")
    if op == '+':
        result=num1+num2
        print(result)
    elif op == '-':
        result=num1-num2
        print(result)
    elif op == '/':
        try:
            result=num1/num2
            print(result)
        except ZeroDivisionError as error:
            print(error)
    elif op =='*':
        result=num1*num2
        print(result)
    else:
        print("invalid operator")
except ValueError:
    print("invalid datatype")
    
    
