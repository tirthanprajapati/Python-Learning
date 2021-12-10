def primecheck(a):
    c=0
    for i in range(1,int(a/2)):
        if(a%i==0):
            c=c+1
    return c

n=int(input(print("Enter a number which is to be checked")))
count = primecheck(n)
if count == 2:
    print("It is a prime number")
else:
    print("It is not a prime nunmber")