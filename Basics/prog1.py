print("Input 3 numbers")
a=float(input("Enter no. 1:"))
b=float(input("Enter no. 2:"))
c=float(input("Enter no. 3:"))

max=0
if a>b and a>c :
    max =a
if b>c and b>a :
    max=b
if c>a and c>b :
    max=c

if a==b and a==c: #can also use a==b==c
    print("All the numbers are same")
else:
    print("The maximum bumber is: ",max)