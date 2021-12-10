#
#
#                             Decimal to Binary through Recursion
#
#

def decobin(num):
    if num>0:
        decobin(num//2)
        print(num%2,end="")
        
n = int(input("Enter a numberehose binary has to be calaculated"))
decobin(n)