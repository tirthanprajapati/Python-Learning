#summ
l=[]
n = int(input("Enter no of inputs"))


for i in range(0,n):
    temp = float(input("enter a no."))
    l.append(temp)


sum=0.0
for i in range(0,n):
    sum=sum+l[i]


print("Sum of the following inputs is: ",sum)