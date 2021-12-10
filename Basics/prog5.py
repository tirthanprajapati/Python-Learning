def fact(a):
    if a==1:
        return 0
    elif a==2:
        return 1
    else:
        return fact(a-1)+fact(a-2)

n=int(input("Enter a number"))
print(":",end="")
if n>=0:
    for i in range(1,n+1):
        print(fact(i),end=":")
else:
    print(f"WRONG INIPUT")