#
#
#                  GCD
#
#

n=int(input("Enter a number"))
b=int(input("Enter a number"))

max=0
if n>b:
    max=n
else:
    max=b
    
maxx=0
for i in range (1,max):
    if(n%i==0):
        if(b%i==0):
            maxx=i
            
            
print("GCD =",maxx)