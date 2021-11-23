import math
import matplotlib.pyplot as plt

def sin_curve():
    sin_curve_list = []
    radian_list = []
    
    for i in range(361):
        radian_list.append(i)
        sin_val = math.sin(math.radians(i))
        sin_curve_list.append(sin_val)
    plt.plot(radian_list, sin_curve_list)
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.axhline(y=0, color='black')
    plt.title("sine curve")
    plt.show()



def cos_curve():
    cos_curve_list = []
    radian_list = []
    
    for i in range(361):
        radian_list.append(i)
        cos_val = math.cos(math.radians(i))
        cos_curve_list.append(cos_val)
    plt.plot(radian_list, cos_curve_list)
    plt.xlabel('x')
    plt.ylabel('cos(x)')
    plt.title("cosine curve")
    plt.axhline(y=0, color='black')
    plt.show()

def input_function():
    degree = input("Enter the degree of the polynimial :")
    valid_input = True
    while valid_input :
        if degree.isnumeric():
            degree = int(degree)
            valid_input = False
        else:
            print("Enter a valid input :")

    coffecient_list = [] 
    for i in range(degree+1):
        coffecient = int(input("Enter the coffecient for x^{}".format(i)))
        coffecient_list.append(coffecient)
    
    return coffecient_list


def plot_polynomial(coffecient_list):
    polynomial_val = []
    x_values = []
    for i in range(10):
        value = 0
        power = 0
        for coffecient in coffecient_list:
            value += coffecient * (i ** power)
            power += 1
        polynomial_val.append(value)
        x_values.append(i)

    plt.plot(x_values,polynomial_val)
    plt.xlabel('x')
    plt.ylabel('polynomial value')
    plt.title("polynimial curve ")
    plt.show()

def exponential_curve():
    polynomial_val = []
    x_values = []
    for i in range(10):
        value = 2**i
        x_values.append(i)
        polynomial_val.append(value)

    plt.plot(x_values, polynomial_val)
    plt.xlabel('x')
    plt.ylabel('Polynomial value')
    plt.title("Exponential curve ")
    plt.show()


def main():
    # sin_curve()
    # cos_curve()
    # coffecient_list = input_function()
    # plot_polynomial(coffecient_list)
    exponential_curve()
main()

