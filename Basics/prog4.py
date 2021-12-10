# fibbonachy series
n=int(input("Enter a number"))

x=0
y=1
z=x+y
print("|",end="")
print(y,end="|")
for i in range(0,n-2):
    print(z,end="|")
    z=x+y
    x=y
    y=z
    

