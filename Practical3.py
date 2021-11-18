#method to return the list with n terms of fibonacci series
def fibonacci_series(n):
    a = 0
    b = 1
    series = [0]
    for i in range(1,n):
        x = a + b
        series.insert(i, x)
        b = a
        a = x
    return series

#method to return the result list
def result(val):
    factorial = 1
    for i in range(val, 1, -1):
        factorial = factorial * i
    result_list = [val, factorial]
    return result_list

def main():
    print("___________________Fibonacci sequence_______________")
    n = input("Enter the number of terms you want to print ")
    if n.isnumeric():
        n = int(n)
    else :
        print("Invalid Input")
        exit()
    if n>=1:
        series = fibonacci_series(n)
        print("Fibbonacci series")
        print(series)
        last_term = series[len(series)-1]
        result_list = result(last_term)
        print("Last term and its factorial :", result_list)
    else:
        print("Number of terms cannot be 0 or less \nIncorrect input")

if __name__ == '__main__':
    main()