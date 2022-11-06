#include <iostream >
using namespace std;

void linear_search_iterative(int list_size, int list[], int search_item) {
	for (int i = 0; i < list_size; i++)
	{
		if (list[i] == search_item) {
			cout << i << "  " << search_item ;
			return;
		}
	}
	cout << -1;
}

int main(int argc, char const *argv[])
{
	int size;
	cin >> size;
	int list[size];

	for (int i = 0; i < size; ++i) {
		cin >> list[size];
	}

	linear_search_iterative(size, list[],10)
	
	return 0;
}