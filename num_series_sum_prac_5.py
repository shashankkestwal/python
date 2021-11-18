def factorial(val):
    factorial=1
    for j in range(val,1,-1):
        factorial=factorial*j
    
    return factorial

def series(x,n):
    sum=0
    import math
    i=0
    while i<=n:
        if (i/2)%2==0:
            sum+=math.pow(x,i)/factorial(i)
            i+=2
        else:
            sum-=math.pow(x,i)/factorial(i)
            i+=2
    return sum

def main(): 
    print("A program to print the series \n1–x2/2!+x4/4!–x6/6!+…xn/n! ")
    x=int(input("Enter the value of x: "))
    n=int(input("Enter the value of n: "))
    if n>=0:
        print("The sum of the series till n is",series(x,n))
    else:
        print("Invalid value of n")

main()

