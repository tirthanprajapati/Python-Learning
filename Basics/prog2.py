def fact(a):
    factoral=1
    for i in range(1,a+1):
        factoral=factoral*i

    return factoral

n=int(input("Enter the number whose factorial is to be calculated"))
f=fact(n)
print("factorial =",fact)