n=int(input("enter a no."))
su=0
num=n
d=0

while num>1:
    d=num%10
    su=su+int(d)
    num=num/10

print("total number of digits are: ",su)