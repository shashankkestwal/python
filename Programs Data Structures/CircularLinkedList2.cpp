#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;

    Node(int el)
    {
        // int data;
        this->data = el;
        this->next = NULL;
    }
};

Node *get_last_element(Node *head)
{
    Node *temp = head;
    if (head->next == NULL)
    {
        return head;
    }

    while (temp->next != head)
    {
        temp = temp->next;
    }
    return temp;
}

bool is_empty123(Node *head)
{
    if (head == NULL)
    {
        return true;
    }
    return false;
}

Node *create_new_node(int data)
{
    Node *new_node = new Node(data);
    return new_node;
}

void insert_at_beginning(Node *head, int data)
{
    Node *new_head = create_new_node(data);
    if (head==NULL)
    {
        head = new_head;
    }

    Node *last_node = get_last_element(head);
    last_node->next = new_head;
    new_head->next = head;
    cout << "Element inserted at the beginning " << endl;
}

void start_list(int data, Node *start_node)
{
    insert_at_beginning(start_node, data);
}

void insert_at_end(Node *head, int data)
{
    Node *last_element = get_last_element(head);
    Node *new_node = create_new_node(data);
    last_element->next = new_node;
    new_node->next = head;
    cout << "Element inserted at the end " << endl;
}

void traverse_list(Node *head)
{
    // if (head->next==head)
    // {
    //     cout<<head->data<<" ";
    // }
    // if (!is_empty123(head))
    // {
    //     Node *temp = head;
    //     do
    //     {
    //         cout << temp->data << "->";
    //         temp = temp->next;
    //     }while (temp->next != head);
    // }else{
    //     cout<<"empty list cannot be traversed"<<endl;
    //     return;
    // }  

    Node* temp = head;
 
    // If linked list is not empty
    if (head != NULL) {
 
        // Print nodes till we reach first node again
        do {
            cout << temp->data << " ";
            temp = temp->next;
        } while (temp != head);
    }
}


int main()
{
    Node *start_node = NULL;
    start_list(10, start_node);
    insert_at_beginning(start_node, 10);
    insert_at_beginning(start_node, 20);
    insert_at_beginning(start_node, 30);
    insert_at_beginning(start_node, 40);
    traverse_list(start_node);
    insert_at_end(start_node, 50);
    insert_at_end(start_node, 60);
   
}