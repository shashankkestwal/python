#include <iostream>
using namespace std;

template<class T> 

int binarySearch (T arr[], T size , T search_element) {
	int low = 0;
	int high = size; 
	int mid;

	while( low <  high ) {
		mid = (low + high) /2;
		if (arr[mid] ==search_element)
		{
			return mid;
		} else if (arr[mid] > search_element) {
			low = mid + 1;
		} else if (arr[mid] < search_element) {
			high = mid ;
		}
	}
	return -1;
}

template <class T>

void inputArray(T arr[], T size) {
	cout << "Enter the elements of array"<<endl;
	for (int i = 0; i < size; i++) {
		cin >> arr[i];
	}
}

int main(int argc, char const *argv[])
{
	int size;
	int arr[size];
	int search_element;
	cout << "Enter the size of array"<<endl;
	cin >> size;
	inputArray(arr, size);
	cout << "Enter the element you want to search "<<endl;
	cin >> search_element;
	int index = binarySearch(arr, size, search_element);
	if (index == -1 ) {
		cout << "Element not found"<<endl;
	} else {
		cout << "Element found at index "<< index <<endl;
	}

	return 0;
}