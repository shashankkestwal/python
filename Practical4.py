def numberset(num):
    print("The return set is :")
    temp = 0
    numset = set()
    
    while num != 0:
        temp = num%10
        numset.add(temp)
        num //= 10   
    
    return numset

def main():
    print("Print the digits in any number")
    num = input("Enter the number (>=10 and <=-10) : ")
    if num.isnumeric():
        num = abs(int(num))
    else:
        print("Invalid input")
        exit()

    if num > -10 and num < 10:
        print("Cannot perform operation on this number")
        exit()
    elif num < 0:
        set_of_numbers = numberset(abs(num))
    else:
        set_of_numbers = numberset(num)
    print (set_of_numbers)

if __name__ == '__main__':
    main()