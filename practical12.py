import matplotlib.pyplot as plt

def histogram(lst):
    nbins = [0,10,20,30,40,50,60,70,80,90,100]
    plt.hist(lst, bins = nbins, ec='grey', color='skyblue')
    plt.xlabel('range')
    plt.ylabel('numbers in list')
    plt.show()

def main():
    lst = []
    n = int(input('Enter the total numbers: '))

    for i in range(0, n):
        ele = input('Enter the number [{}] in smaller than 100  '.format(i+1))
        lst.append(int(ele))
    histogram(lst)

if __name__ == '__main__':
    main()
