#input a number and print its sum of series
# series s=(1/1!)+(2/2!)+......n times


n = int(input(print(f"Enter the value of N(ie. the number of term till which the loop must run)")))


def fact(a):
    product=1
    for i in range(1,a+1):
        product=product*i
    return product


sum=0
for i in range(1,n+1):
    sum=sum+(n/int(fact(n)))
print(f"The final Sum of the series is ", end='')
print(sum)