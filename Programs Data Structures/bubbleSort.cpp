#include<iostream>  
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
void bubblesort(T a[],int size){
    int i, j,temp; 
    for(i = 0; i<size; i++)  {  
            for(j = i+1; j<size; j++)  
            {  
                if(a[j] < a[i])  
                {  
                    temp = a[i];  
                    a[i] = a[j];  
                    a[j] = temp;   
                }   
            }   
        }   
    }


int main ()  
{    
    cout<<"Enter the number of elements of the array :";
    int size;
    cin>>size;
    int a[size];
    cout<<"Enter the array elements: \n";
    for (int i = 0; i < size; i++)
    {
        cin>>a[i];
    }
    
    cout<<"array before sorting"<<endl;   
    printArr(a,size);
    bubblesort(a,size);
    cout<<"array after sorting"<<endl;
    printArr(a,size);
    return 0;  
}  