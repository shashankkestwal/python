#include <iostream>
using namespace std;


class Queue {
    public:
    
    
    int i = 0;
    int n = 5;
    int arr[5];
    

    void isEmpty(){
        if (i == 0 ) {
            cout<<"Empty queue";
        }  
    }
    void enqueue (int data) {
        if (i < n) {
            this->arr[i] = data;
            i++;
        } else {
            cout<<"Queue full";
        }
    }
    void dequeue (int data) {
        for (int j = 0; j < i; j++) {
            this->arr[j] = this->arr[j+1];
        }
        i--;
    }
    void peek(){
        cout<<this->arr[0];
    }

    void traverse() {
        for (int j = 0; j < i; j++){
            cout<<this->arr[j]<<"  ";
        }
    }
};

int main(int argc, char const *argv[])
{
    Queue q1;
    cout << "------------- Implementation of queue using array -------------" << endl;

    int choice;
    char more;
    do
    {
        cout<<"(i)Enqueue in queue"<<endl
            <<"(ii)Dequeue in queue "<<endl
            <<"(iii)Peek in queue "<<endl
            <<"(iv)Traverse in queue"<<endl;
        cout << "Enter your choice "<<endl;
        cin >> choice;
        switch (choice)
        {
        case 1:
            int element;
            cout<<"Enter the element you want to enqueue :" ;
            cin>>element;
            q1.enqueue(element);
            break;
        case 2:
            q1.dequeue(element);
            break;
        case 2:
            q1.peek(element);
            break;
        case 4:
            q1.traverse();
        default:
            break;
        }
    } while (more != 'n' && more != 'N');
    
    return 0;
}
