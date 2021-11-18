def salesman_details(sales):   
    if(sales < 40000):
        remarks = "Work Hard"
    elif(sales >= 40000 and sales < 60000):
        remarks="Average Sales"
    elif(sales >= 60000 and sales < 80000):
         remarks = "Good Sales"
    elif(sales >= 80000):
         remarks = "Excellent Sales"
    if sales < 50000:
        print("Your sale for this month is less then 50000\nNo commission is rewarded")
        commission = 0
    else:
        commission = sales*5/100
    salesman_status = [sales,remarks,commission]
    return salesman_status

def main():
    print("Welcome salesman ")
    choice = ''
    while choice != 'n' and choice !='N':
        sales=input("Enter your sales for the week: ")
        if sales.isnumeric():
            sales = int(sales)
        else :
            print("Invalid Input")
            exit()
        sales=int(sales*30/7)
        if sales>=0:
            salesman_info = salesman_details(sales)
            print("---Your report for the month--- ")
            sales_data = ["sales"   , "remarks"   ,   "commission"]      
            print(sales_data)
            print(salesman_info)
        else:
            print("Incorrect input")
        choice = input("Do you want to continue :")


if __name__ == '__main__':
    main()
