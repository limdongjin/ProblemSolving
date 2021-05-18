#include <iostream>

using namespace std;

class Node {
    public:
        int v;
        Node* next;
        Node* prev;

        Node(int a){
            this->v = a;
        }

        static Node* linkedlist(int n){
            Node* head = new Node(1);
            Node* cur = head;

            for(int i=2;i<=n;i++){
                Node* nnode = new Node(i);
                nnode->prev = cur;
                cur->next = nnode;

                cur = nnode;
            }
            cur->next = head;
            head->prev = cur;

            return head;
        }

        static Node* remove_node(Node* node){
            node->prev->next = node->next;
            node->next->prev = node->prev;

            return node->next;
        }

        static void print_node(Node* node){
            Node* cur = node;
            
            while(cur != nullptr){
                cout << cur->v << " ";
                cur = cur->next;
                if(cur == node) break;
            }
            cout << "\n";
        }
};

void josephus(int n, int k){
    Node* l = Node::linkedlist(n);
    Node* cur = l;

    while(cur != nullptr){
        if(cur->next->next == cur) break;
        cur = Node::remove_node(cur);

        for(int i=0;i<k-1;i++)
            cur = cur->next;
    }
    int a=cur->v, b=cur->next->v;
    if(b > a){
        cout << a << " " << b << endl;
        return;
    }
    cout << b << " " << a << endl;
}

int main(){
    int c;
    cin >> c;
    
    while(c){
        c--;
        int n, k;
        cin >> n >> k;
        josephus(n, k);
    }
}
