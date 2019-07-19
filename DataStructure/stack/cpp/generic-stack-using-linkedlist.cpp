#include <cstdio>
#include <iostream>
#include <typeinfo>

/* Test Function */
void test_float_stack_all_features();
void test_int_stack_all_features();

template <class TStack> class Stack {
    private:
        struct Node {
            TStack value_;
            Node* next_;
            Node(TStack value){
                this->value_ = value;
                this->next_ = nullptr;
            }
            void set_next(Node* nodePtr){
                this->next_ = nodePtr;
            }
        };
        int size_;
        Node* top_;
    public:
        Stack(){
            this->size_ = 0;
            this->top_ = nullptr;
        }
        void push(TStack value);
        TStack pop();
        TStack top();
        bool is_empty();
        void print();
        int size();
};

template <class TStack> void Stack<TStack>::push(TStack value){
    Stack::Node* node = new Stack::Node(value);

    node->set_next(this->top_);
    this->top_ = node;
    this->size_++;
}

template <class TStack> TStack Stack<TStack>::pop(){
    assert(!is_empty());
    Stack::Node* node;

    node = this->top_;
    TStack node_value = node->value_;

    this->top_ = this->top_->next_;

    delete node;
    this->size_--;

    return node_value;
}

template <class TStack> TStack Stack<TStack>::top(){
    assert(!this->is_empty());

    return this->top_->value_;
}

template <class TStack> bool Stack<TStack>::is_empty(){
    return this->size_ == 0;
}

template <class TStack> void Stack<TStack>::print(){
    if(is_empty()){
        std::cout << "NULL STACK" << std::endl;
        return;
    }

    Stack::Node* cur = this->top_;
    while(cur->next_ != nullptr){
        std::cout << cur->value_ << " -> ";
        cur = cur->next_;
    }
    std::cout << cur->value_ << std::endl;
}
template <class TStack> int Stack<TStack>::size(){
    return this->size_;
}

int main(){
    test_float_stack_all_features();
    test_int_stack_all_features();
}

void test_float_stack_all_features(){
    Stack<float> floatStack;
    assert(floatStack.is_empty());

    floatStack.push(11.11);
    assert(!floatStack.is_empty());
    assert(floatStack.top() == 11.11f);
    assert(floatStack.size() == 1);
    floatStack.print();

    floatStack.push(122.215);
    assert(floatStack.top() == 122.215f);
    assert(floatStack.size() == 2);
    floatStack.print();

    assert(floatStack.pop() == 122.215f);
    assert(floatStack.top() == 11.11f);
    assert(floatStack.size() == 1);
    floatStack.print();

    assert(floatStack.pop() == 11.11f);
    assert(floatStack.size() == 0);

    floatStack.print();
}

void test_int_stack_all_features(){
    Stack<int> intStack;
    assert(intStack.is_empty());

    intStack.push(789);
    assert(!intStack.is_empty());
    assert(intStack.top() == 789);
    assert(intStack.size() == 1);
    intStack.print();

    intStack.push(45);
    assert(intStack.top() == 45);
    assert(intStack.size() == 2);
    intStack.print();

    assert(intStack.pop() == 45);
    assert(intStack.top() == 789);
    assert(intStack.size() == 1);
    intStack.print();

    assert(intStack.pop() == 789);
    assert(intStack.size() == 0);

    intStack.print();
}
