#
#
#                                   Binary to Decimal
#
#

n = int(input(print("Enter a value whose decimal has to be calaculated")))
num=n
i=0
res=0
deci_digi=0
while num>0:
    res=num%10
    deci_digi=deci_digi+((2**i)*res)
    num=num//10
    i=i+1
    
print(deci_digi)