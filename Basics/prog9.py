def factorial(a):
    p=1
    for i in range(1,a+1):
        p=p*i
    
    return p


a=int(input("Enter the number whose factorial is to be calculated"))
print("factorial: ",factorial(a))