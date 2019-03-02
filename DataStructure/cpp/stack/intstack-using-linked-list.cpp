#include <cstdio>
#include <cassert>
#include <iostream>
using namespace std;
class Node {
public:
    int value = -1;
    Node* prev = nullptr;
    Node(int value){
        this->value = value;
        this->prev = nullptr;
    };
};
class IntStack {
private:
    int size_ = 0;
    Node* top_;
public:
    IntStack(){
        this->top_ = nullptr;
        this->size_ = 0;
    }
    IntStack(int value){
        Node* element = new Node(value);
        this->top_ = element;
        this->size_ = 1;
    }
    int top(){
        if(this->isEmpty()) throw range_error("stack is empty");
        return this->top_->value;
    }
    int pop(){
        if(this->isEmpty()) throw range_error("stack is empty");

        Node* topElem = this->top_;
        this->top_ = this->top_->prev;
        (this->size_)--;
        return topElem->value;
    }
    void push(int value){
        Node* element = new Node(value);
        Node* prevElem = this->top_;
        this->top_ = element;
        this->top_->prev = prevElem;
        (this->size_)++;
    }
    bool isEmpty(){
        return this->size_ == 0;
    }
    int size(){
        return this->size_;
    }
};
void TestIntStack();
int main(){
    TestIntStack();
}
void TestIntStack(){
    IntStack* stack = new IntStack(99);
    assert(stack->top() == 99);
    stack->push(1121);
    assert(stack->top() == 1121);
    assert(stack->size() == 2);
    assert(stack->pop() == 1121);
    assert(stack->size() == 1);
    assert(stack->pop() == 99);
    assert(stack->size() == 0);
    assert(stack->isEmpty());
    cout << "Test Success!" << endl;
}