def fibbonacci_series(n):
    a=0
    b=1
    series=[0]
    for i in range(1,n):
        x=a+b
        series.append(x)
        b=a
        a=x
    return series
def factorial(val):
    factorial=1
    for i in range(val,1,-1):
        factorial=factorial*i
    return factorial

def main():
    print("___Fibonacci sequence___")
    n=int(input("Enter the number of terms you want to print "))
    if n>=1:
        print("Fibbonacci series")
        print(fibbonacci_series(n))
        last_term=fibbonacci_series(n).pop()
        print("nth term of Fibonacci sequence ",last_term)
        print("Factorail of",last_term," is ",factorial(last_term))
    else:
        print("Number of terms cannot be 0 or less \nIncorrect input")
main()