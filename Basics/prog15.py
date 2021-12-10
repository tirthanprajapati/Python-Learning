#
#
#                                   Decimal to Binary
#
#

n = int(input(print("Enter a value whose binary has to be calculated")))
num=n
res=1
ress=""
while num>0:
    res=num%2
    ress=ress+str(res)
    num=num//2
    
print(ress[::-1])