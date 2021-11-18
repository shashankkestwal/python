#include <iostream>
using namespace std;


template<class T>
void printArr(T array[],int size){
    for (int i = 0; i < size; i++)
    {
        cout<<array[i]<<"   ";
    }
    cout<<endl;
    
}

template<class T>
void insertionSort(T array[],int size ){
    
    T temp;
    for (int i = 1, j ; i < size; i++)
    {
        temp=array[i];
        for ( j = i ; j > 0   ; j--)
        {       
            if (temp < array[j-1])
            {
              array[j]=array[j-1];  
            }else{
                break;
            }
        }
        array[j]=temp;
    }
    
}



int main(int argc, char const *argv[])
{
    int array[] = {1,4,6,2,8};
    int size=sizeof(array)/sizeof(int);
    cout<<"array before sorting"<<endl;
    printArr(array,size);
    
    cout<<"array after sorting"<<endl;
    insertionSort(array,size);
    printArr(array,size);
    return 0;
}
