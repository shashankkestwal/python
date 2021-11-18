def numberset(num):
    print("The return set is :")
    temp=0
    numset=list()
    
    while num!=0:
        temp=num%10
        numset.append(temp)
        num//=10   
    for i in range(len(numset)-1,-1,-1):
        print(numset[i],end=" ")
    print(reversed(numset))
def main():
    num=abs(int(input("Enter the number: ")))
    if num>0 and num<10:
        print("Cannot perform operation on this number")
    elif num<0:
        numberset(abs(num))
    else:
        numberset(num)
    
main()