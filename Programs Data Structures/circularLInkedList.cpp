#include <iostream>
using namespace std;

template <class T>

class Node
{
public:
    T data;
    Node<T> *next;

    Node<T>(T el)
    {
        data = el;
        next = NULL;
    }
};

class circularLInkedList
{
public:
// Node<T> *head;
template <class T>
Node<T> *insertAtHead(Node<T> *head, T el)
{
    Node<T> *n = new Node<T>(el);
    if (head == NULL)
    {
        head = n;
        head->next = head;
        return head;
    }

    Node<T> *last_element = head;
    while (last_element->next != head)
    {
        last_element = last_element->next;
    }

    n->next = head;
    last_element->next = n;

    return n;
}

template <class T>
void display(Node<T> *head)
{
    if (head == NULL)
    {
        cout << "Empty linked list" << endl;
        return;
    }

    Node<T> *temp = head;

    if (temp->next == head)
    {
        cout << temp->data;
    }
    else
    {
        while (temp->next != head)
        {
            cout << temp->data;
            cout << "->";
            temp = temp->next;
        }
        cout << temp->data;
    }
    cout << endl;
}

template <class T>
int search_in_list(Node<T> *head, T el)
{
    int position = 1;
    if (head == NULL)
    {
        return -1;
    }
    Node<T> *temp = head;
    do
    {
        if (temp->data == el)
        {
            return position;
        }
        temp = temp->next;
        position++;
    } while (temp != head);
    return -1;
}

template <class T>
void insertAfterPosition(Node<T> *head, T elementToEnter, int pos)
{
    if (pos == -1)
    {
        return;
    }
    else
    {
        if (head == NULL)
        {
            cout << "List is empty";
            return;
        }
        Node<T> *n = new Node<T>(elementToEnter);
        Node<T> *temp = head;
        for (int i = 1; i < pos; i++)
        {
            if (temp->next == head)
            {
                cout << "List is shorter then the input index " << endl;
                return;
            }
            temp = temp->next;
        }
        Node<T> *newTemp = temp->next;
        temp->next = n;
        n->next = newTemp;
    }
}

template <class T>
Node<T> *insertAtEnd(Node<T> *head, T elementToEnter)
{
    Node<T> *n = new Node<T>(elementToEnter);
    if (head == NULL)
    {
        head = insertAtHead(head, elementToEnter);
        return head;
    }

    Node<T> *temp = head;
    do
    {
        temp = temp->next;
    } while (temp->next != head);
    temp->next = n;
    n->next = head;
    return head;
}

template <class T>
Node<T> *deleteFromStart(Node<T> *head)
{
    if (head == NULL)
    {
        cout << "Operation not possible" << endl;
        return head;
    }

    Node<T> *temp = head;
    Node<T> *new_head;
    while (temp->next != head)
    {
        temp = temp->next;
    }

    if (temp == head)
    {
        delete head;
        return NULL;
    }
    else
    {
        temp->next = head->next;
        delete head;
        return temp->next;
    }
}
template <class T>
Node<T> *deleteFromEnd(Node<T> *head)
{
    if (head == NULL)
    {
        cout << "Operation not possible" << endl;
        return NULL;
    }
    else if (head->next == head)
    {
        return NULL;
    }
    else
    {
        Node<T> *temp = head;
        while (temp->next->next != head)
        {
            temp = temp->next;
        }
        temp->next = head;
        return head;
    }
}

template <class T>
Node<T> *removeNodeWithGivenElement(Node<T> *head, int pos)
{

    if (pos == -1)
    {
        cout << "Operation not possible" << endl;
        return head;
    }
    else if (pos == 1)
    {
        head = deleteFromStart(head);
        return head;
    }
    else
    {
        Node<T> *temp = head;
        for (int i = 1; i < pos - 1; i++)
        {
            if (temp->next == head)
            {
                cout << "List is shorter then the input index " << endl;
                return head;
            }
            temp = temp->next;
        }

        temp->next = temp->next->next;
        return head;
    }
}

template <class T>
void printPointerOfPos(Node<T> *head, int pos)
{

    Node<T> *temp = head;
    for (int i = 1; i < pos; i++)
    {
        if (temp->next == head)
        {
            cout << "List is shorter then the input index " << endl;
            return;
        }
        temp = temp->next;
    }
    cout << "Element found at position " << pos << " and its pointer is ";
    cout << temp->next << endl;
}

template <class T>
Node<T> *createNewLinkedList(Node<T> *head1)
{
    head1 = insertAtHead(head1, 3);
    head1 = insertAtHead(head1, 2);
    head1 = insertAtHead(head1, 1);
    return head1;
}

template <class T>
void concatenateTwoStrings(Node<T> *head, Node<T> *head1)
{
    if (head == NULL)
    {
        cout << "Empty linked list cannot be concatenated " << endl;
        return;
    }
    else
    {
        Node<T> *temp1 = head;
        Node<T> *temp2 = head1;
        while (temp1->next != head)
        {
            temp1 = temp1->next;
        }
        while (temp2->next != head1)
        {
            temp2 = temp2->next;
        }
        temp2->next = head;
        temp1->next = head1;
        cout << "Both linked list concatenated successfully" << endl;
    }
}
    
};





int main(int argc, char const *argv[])
{

    cout << "-------CPP program implementing a linked list------- " << endl
         << endl;
    Node<int> *head = NULL;
    circularLInkedList cll;
    cout << "An empty linked list is created" << endl;
    char more;
    int element, position, search;

    do
    {
        cout << "(i) Insert an element at the beginning of the circular linked list" << endl
             << "(ii) Insert an element x after an element y in the circular linked list" << endl
             << "(iii)Insert an element at the end of the circular linked list" << endl
             << "(iv) Remove an element from the back of the circular linked list." << endl
             << "(v) Remove an element from the front of the circular linked list." << endl
             << "(vi) Remove the element x from the circularly linked list " << endl
             << "(vii)Search for an element x in the circularly linked list and return its pointer" << endl
             << "(viii) Concatenate two circularly linked lists" << endl
             << endl; 

        int choice;
        cout << "Enter which operation you want to peform : ";
        cin >> choice;
        switch (choice)
        {
        case 1:
            cout << "Enter the element you want to enter : ";
            cin >> element;

            head = cll.insertAtHead(head, element);

            cout << "Element successfully inserted at head" << endl;
            cll.display(head);
            break;
        case 2:

            cout << "Enter the element you want to enter : ";
            cin >> element;
            cout << "Enter the element whose next the given element  must reside : ";
            cin >> search;

            if (cll.search_in_list(head, search) == -1)
            {
                cout << "No element as " << search << " in the list" << endl;
                break;
            }

            cll.insertAfterPosition(head, element, cll.search_in_list(head, search));
            cll.display(head);
            break;
        case 3:
            cout << "Enter the element you want to enter : ";
            cin >> element;
            head = cll.insertAtEnd(head, element);
            cll.display(head);
            break;
        case 4:
            head = cll.deleteFromStart(head);
            cll.display(head);
            break;
        case 5:
            head = cll.deleteFromEnd(head);
            cll.display(head);
            break;
        case 6:
            cout << "Enter Element you want to remove :";
            cin >> search;
            head = cll.removeNodeWithGivenElement(head, cll.search_in_list(head, search));
            cll.display(head);
            break;
        case 7:
            cout << "Enter which element's pointer you want to print :";
            cin >> search;
            position = cll.search_in_list(head, search);
            if (position == -1)
            {
                cout << "Element Not found in the list " << endl;
                break;
            }
            else
            {
                cll.printPointerOfPos(head, position);
            }
            break;
        case 8:
        {
            Node<int> *head1 = NULL;
            head1 = cll.createNewLinkedList(head1);
            cout << "A second linked list is created " << endl;
            cll.display(head1);
            cll.concatenateTwoStrings(head, head1);

            cll.display(head);
        }
        break;

        default:
            cin.clear();
            cout << "Invalid input" << endl;
            break;
        }
        cout << "Do you want to continue operations on linked list, press n/N to exit : ";
        cin >> more;

        cout << endl
             << endl;
    } while (more != 'n' && more != 'N');
    return 0;
}
