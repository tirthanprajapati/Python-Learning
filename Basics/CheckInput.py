# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

Sequen = []

N = int(input(print(f"Enter no. of inputs")))

for i in range(1,N+1):
    temp=int(input(print("Entery No: ",i)))
    Sequen.append(temp)

flag=0

for i in range(0,N-1):
    for j in range(0,N-(i+1)):
        if int(Sequen[j]) == int(Sequen[j+1]):
            flag=1


if flag==0:
    print(f"All the numbers are different in your entries")
if flag==1:
    print(f"All the numbers are not different in your entries")


# if len(data) == len(set(data)):.
# set() function is used to sort the list and remove the reoccuring elements