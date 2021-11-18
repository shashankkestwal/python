// C++ program to illustrate If statement
#include<iostream>
using namespace std;
int isGreater(int x,int y){
	if (x>y)
	{
		return x;
	}else{
		return y;
	}
	
}
int main(int argc, char * const argv[]){
		
		// even the file name is taken as a command line argument in cpp;
		//argc -> number of arguments  
		//argv -> arguments array 
		cout<<"argument counts "<<argc<<endl;
		cout<<argv[0]<<endl;


		//a simple function example:->
		int i = 10;
        int j=9;
        int x=i-j;
        cout<<isGreater(i,j)<<" is greater"<<endl;

		//arrays in cpp

		int arr[10];
		cout<<"Creating and printing an array "<<endl;
		for (int i = 0; i < 10; i++)
		{
			arr[i]=i;
			if (i==9)
			{
				cout<<arr[i];
			}else{
				cout<<arr[i]<<" -> ";
			}
			
			
		}
		cout<<endl;
		//if we would access any index that is not present in the array then we will get any garbage value . Here is an example 

		cout<<endl<<arr[90]<<endl;


		//sizes of some primitive data types in CPP
		cout<<"sizes of some primitive data types for C++"<<endl;
		cout<<sizeof(int)<<" bytes ---> int" <<endl;
		cout<<sizeof(void)<<" byte  ---> void" <<endl;
        cout<<sizeof(wchar_t)<<" bytes ---> wide character"<<endl;
		cout<<sizeof(double)<<" bytes ---> double" <<endl;
		cout<<sizeof(float)<<" bytes ---> float" <<endl;
		cout<<sizeof(bool)<<" byte  ---> bool" <<endl;
		cout<<sizeof(char)<<" byte  ---> char" <<endl;
		

		//String is a character array .The length of the C++ string can be changed at runtime because of dynamic allocation of memory similar to vectors. 
		//For more info on strings refer to stringKnowledgeGFG.cpp

		
		 // Declare an array
    int val[3] = { 5, 10, 15};
 
    // Declare pointer variable
    int *ptr;
 
    // Assign address of val[0] to ptr.
    // We can use ptr=&val[0];(both are same)
    ptr = &val[0] ;
    cout << "Elements of the array are: ";
    cout << ptr[0] << " " << ptr[1] << " " << ptr[2];
		
	

		return 0;
}
