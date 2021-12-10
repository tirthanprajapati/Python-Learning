def fact(a):
    if a==0 :
        return 1
    elif a==1 :
        return 1
    else:
        return a*fact(a-1)

n=int(input("Enter the number whose factorial is to be calculated"))
f=fact(n)
print("factorial =",f)
