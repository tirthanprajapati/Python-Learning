from typing import List


Llist=[]
a = int(input("Enter no of entries in the list"))

i=0
for i in range(0,a):
    x = int(input("Entery a no: "))
    Llist.append(x)


i=0
print("Here is your List")
for i in range(0,a):
    print(Llist[i],end=" /")

    