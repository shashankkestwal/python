def perimeter_triangle(a,b,c):
    
    perimeter=a+b+c
    if(perimeter/2<=a or perimeter/2<=b or perimeter/2<=c):
        print("Triangle not possible ")
        exit()
    else:
        return perimeter

def area_triangle(a,b,c,s):
    import math
        
    area_squared=s*(s-a)*(s-b)*(s-c)
    area=math.sqrt(area_squared)
    return area

def check_sides_sum(side1,side2,side3):
    if(side1>side2 and side1>side3 ):
        assert  side1<side2+side3, "sum of the length of any two sides is greater than the third side."
    elif(side2>side1 and side2>side3):
        assert  side2<side1+side3, "sum of the length of any two sides is greater than the third side."
    else:
        assert side3<side1+side2, "sum of the length of any two sides is greater than the third side."


def main():
    print("Python program to calculate the area of a triangle \n")
    side1=int(input("Enter the length of the first side of a triangle: "))
    side2=int(input("Enter the length of the second side of a triangle: "))
    side3=int(input("Enter the length of the third side of a triangle: "))

    if(side1>0 and side2>0 and side3>0):
        check_sides_sum(side1,side2,side3)
        perimeter=perimeter_triangle(side1,side2,side3)
        print("The perimeter of the triangle is: ",perimeter)
        area=area_triangle(side1,side2,side3,perimeter/2)
        print("The area of the triangle is: ",area)

        
    else:
        print("Invalid inputs !!")
    
main()