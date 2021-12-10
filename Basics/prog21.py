#
#
#                Smallest Divisor
#
#


n=int(input("Enter a number"))
temp=0
min=n

for i in range(2,n):
    if n%i==0:
        temp=i
        if min>=temp:
            min=temp
            
            
print( "Smallest Divisor =" , min)