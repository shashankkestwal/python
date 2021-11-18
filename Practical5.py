import Factorial
import math
def series(x,n):
    sum = 0
    
    i = 0
    while i<=n:
        if (i/2)%2 == 0:
            sum += math.pow(x,i)/Factorial.factorial(i)
            i += 2
        else:
            sum -= math.pow(x,i)/Factorial.factorial(i)
            i += 2
    return sum

def main(): 
    print("A program to print the series \n1–x^2/2!+x^4/4!–x^6/6!+…x^n/n!")
    x = input("Enter the value of x: ")
    if x.isnumeric():
        x = int(x)
    else:
        print("Invalid input")
        exit()
    n = input("Enter the value of n: ")
    if n.isnumeric():
        n = int(n)
    else:
        print("Invalid input")
        exit()
    if n >= 0:
        print("The sum of the series till n is",series(x,n))
    else:
        print("Invalid value of n")

if __name__ == '__main__':
    main()

