def salesman_details(sales):
    
    if(sales<40000):
        remarks="Work Hard"
    elif(sales>=40000 and sales<60000):
        remarks="Average Sales"
    elif(sales>=60000 and sales<80000):
         remarks="Good Sales"
    elif(sales>=80000):
         remarks="Excellent Sales"
    if sales<50000:
        print("Your sale for this month is less then 50000\nNo commission is rewarded")
        commission=0
    else:
        commission=sales*5/100
    salesman_tuple=(sales,remarks,commission)
    return salesman_tuple

def main():
    print("Welcome salesman :)")
    sales=int(input("Enter your sales for the week: "))
    sales=sales*30/7
    if sales>=0:
        print("---Your report for the week--- ")
        
        print(salesman_details(sales))
        print("(sales   , remarks   ,   commission)")
    else:
        print("Incorrect input")

main() 
    
