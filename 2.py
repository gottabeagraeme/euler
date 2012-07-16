secondlast = 0
last = 1
sum=0

fib = secondlast + last

while fib <= 4000000:
    secondlast=last
    last=fib
    fib= secondlast + last
    if (fib%2==0):
        sum=sum+fib
    print ("Fib: " + str(fib))
print (sum)
