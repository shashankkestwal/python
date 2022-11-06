import math
def area_and_perimeter_triangle(a,b,c): 
    perimeter = a + b + c
    s = perimeter/2 
    if(s <= a or s <= b or s <= c):
        print("Triangle not possible ")
        exit()

    area_squared = s*(s - a)*(s - b)*(s - c)
    area = math.sqrt(area_squared)
    t_area_perimeter = {area, perimeter}
    return t_area_perimeter
    
def check_sides_sum(side1,side2,side3):
    if(side1 > side2 and side1 > side3 ):
        assert  side1 < side2 + side3, "sum of the length of any two sides is greater than the third side."
    elif(side2>side1 and side2>side3):
        assert  side2 < side1 + side3, "sum of the length of any two sides is greater than the third side."
    else:
        assert side3 < side1 + side2, "sum of the length of any two sides is greater than the third side."


def main():
    print("Python program to calculate the area of a triangle \n")
    side1 = input("Enter the length of the first side of a triangle: ")
    if side1.isnumeric():
        side1 = int(side1)
    else:
        print("Invalid input")
        exit()
    side2 = input("Enter the length of the second side of a triangle: ")
    if side2.isnumeric():
        side2 = int(side2)
    else:
        print("Invalid input")
        exit()
    side3 = input("Enter the length of the third side of a triangle: ")
    if side3.isnumeric():
        side3 = int(side3)
    else:
        print("Invalid input")
        exit()
    if(side1 > 0 and side2 > 0 and side3 > 0):
        check_sides_sum(side1, side2, side3)
        t_area_perimeter = area_and_perimeter_triangle(side1, side2, side3)
        
        print("{area, perimerter} :",end="")
        print(t_area_perimeter)

    else:
        print("Invalid inputs !!")
    
if __name__ == '__main__':
    main()