#
#
#                                   Decimal to HexaDecimal
#
#

aba = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']

n = int(input(print("Enter a value whose binary has to be calculated")))
num=n
res=1
ress=""
while num>0:
    res=int(num%16)
    xyz=aba[res]
    if isinstance(aba[res], int):
        xyz=str(res)
    ress=ress+xyz
    num=num//16
    
print(ress[::-1])