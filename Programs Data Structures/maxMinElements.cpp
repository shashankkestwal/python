#include <iostream>
#include <math.h>
#include <climits>

using namespace std;
void minMax(int array[], int n){
    int minVal = INT_MAX;
    int maxVal =INT_MIN;
    if (n==1)
    {
        minVal=array[0];
        maxVal=array[0];
    }else if (n > 1 || n <= pow(10,5))
    {
        for (int i = 0; i < n; i++)
        {
            if (array[i]<minVal)
            {
                minVal=array[i];
            }
            if (array[i]>maxVal)
            {
                maxVal=array[i];
            }
            
        }  
    }
    cout<<"min = "<<minVal<<", max =  "<<maxVal;
    
}

int main(int argc, char const *argv[])
{
    int n;
    cout<<"enter size"<<endl;
    cin>>n;
    int array[n];
    cout<<"Enter the array elements"<<endl;
    for (int i = 0; i < n; i++)
    {
        int element;
        cin>>element;
        if (element >= 1 || element<=pow(10,12))
        {
            element=array[i];
        }else{
            return 0;
        }       
    }
    minMax(array,n);
    
    return 0;
}
