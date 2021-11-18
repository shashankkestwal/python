#include <iostream>
using namespace std;

void mergedArray(int array1[], int array2[], int size1, int size2)
{

    int mergedSize = size1 + size2;
    int mergedArray[mergedSize];
    int i = 0, j = 0;
    int k = 0;
    //compairing elements and adding in merged array
    while (i < size1 && j < size2 && k < mergedSize)
    {
        if (array1[i] <= array2[j])
        {
            mergedArray[k] = array1[i];
            i++, k++;
        }
        else
        {
            mergedArray[k] = array2[j];
            j++, k++;
        }
    }

    //copying the remaining elements in merged array.
    while (i < size1)
    {
        mergedArray[k] = array1[i];
        i++, k++;
    }
    while (j < size2)
    {
        mergedArray[k] = array2[j];
        j++, k++;
    }
    for (int i = 0; i < mergedSize; i++)
    {
        cout << mergedArray[i] << " ";
    }
}

int main(int argc, char const *argv[])
{
    int array1[] = {1, 5, 6, 8, 9};
    int array2[] = {2, 4, 6, 7, 8, 10};
    int size1 = sizeof(array1)/sizeof(int);
    int size2 = sizeof(array1)/sizeof(int);
    cout << "The merged array is ";
    if (size1 > 0 && size2 > 0)
    {
        mergedArray(array1, array2, size1, size2);
    }
    return 0;
}
