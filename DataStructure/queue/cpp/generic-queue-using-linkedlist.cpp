#include <iostream>

void test_int_queue_all_features();
void test_float_queue_all_features();

template <class TQueue> class Queue {
private:
    struct Node {
        TQueue value_;
        Node* next_;
        Node(TQueue value){
            this->value_ = value;
            this->next_ = nullptr;
        }
        void set_next(Node* next){
            this->next_ = next;
        }
    };
    int size_;
    Node* front_;
    Node* rear_;
public:
    Queue(){
        this->size_ = 0;
        this->front_ = nullptr;
        this->rear_ = nullptr;
    }
    void push(TQueue value);
    TQueue pop();
    bool is_empty();
    int size();
    void print();
    TQueue front();
    TQueue rear();
};

template <class TQueue> void Queue<TQueue>::push(TQueue value){
    this->size_++;

    Node* nodePtr = new Node(value);

    if(this->is_empty()){
        this->front_ = nodePtr;
        this->rear_ = nodePtr;
        return;
    }

    this->rear_->set_next(nodePtr);
//    nodePtr->set_next(this->rear_);
    this->rear_ = nodePtr;
}

template <class TQueue> TQueue Queue<TQueue>::pop(){
    assert(!this->is_empty());

    TQueue node_value = this->front_->value_;
    Node* node = this->front_;

    this->front_ = this->front_->next_;
    this->size_--;

    delete node;

    return node_value;

}

template <class TQueue> bool Queue<TQueue>::is_empty(){
    return this->front_ == nullptr;
}

template <class TQueue> int Queue<TQueue>::size(){
    return this->size_;
}

template <class TQueue> void Queue<TQueue>::print(){
    if(this->is_empty()){
        std::cout << "NULL STACK" << std::endl;
        return;
    }

    Node* cur = this->front_;
    std::cout << "front ";
    while(cur->next_ != nullptr){
        std::cout << cur->value_ << " -> ";
        cur = cur->next_;
    }
    std:: cout << cur->value_ << " rear"<< std::endl;
}

template <class TQueue> TQueue Queue<TQueue>::front(){
    assert(!this->is_empty());

    return this->front_->value_;
}
template <class TQueue> TQueue Queue<TQueue>::rear(){
    assert(!this->is_empty());

    return this->rear_->value_;
}

int main(){
    test_int_queue_all_features();
    test_float_queue_all_features();
}

void test_int_queue_all_features(){
    Queue<int> intQueue;

    intQueue.push(1);
    intQueue.print();

    assert(intQueue.front() == 1);
    assert(intQueue.rear() == 1);

    intQueue.push(2);
    intQueue.print();
    assert(intQueue.front() == 1);
    assert(intQueue.rear() == 2);
    assert(intQueue.size() == 2);

    intQueue.push(3);
    intQueue.print();
    assert(intQueue.front() == 1);
    assert(intQueue.rear() == 3);
    assert(intQueue.size() == 3);

    intQueue.pop();
    intQueue.print();
    assert(intQueue.front() == 2);
    assert(intQueue.rear() == 3);
    assert(intQueue.size() == 2);

    intQueue.pop();
    intQueue.print();
    assert(intQueue.front() == 3);
    assert(intQueue.rear() == 3);
    assert(intQueue.size() == 1);

    intQueue.pop();
    intQueue.print();
    assert(intQueue.is_empty());
    assert(intQueue.size() == 0);
}

void test_float_queue_all_features(){
    Queue<float> floatQueue;

    floatQueue.push(1.1);
    floatQueue.print();

    assert(floatQueue.front() == 1.1f);
    assert(floatQueue.rear() == 1.1f);

    floatQueue.push(2.2);
    floatQueue.print();
    assert(floatQueue.front() == 1.1f);
    assert(floatQueue.rear() == 2.2f);
    assert(floatQueue.size() == 2);

    floatQueue.push(3.3);
    floatQueue.print();
    assert(floatQueue.front() == 1.1f);
    assert(floatQueue.rear() == 3.3f);
    assert(floatQueue.size() == 3);

    floatQueue.pop();
    floatQueue.print();
    assert(floatQueue.front() == 2.2f);
    assert(floatQueue.rear() == 3.3f);
    assert(floatQueue.size() == 2);

    floatQueue.pop();
    floatQueue.print();
    assert(floatQueue.front() == 3.3f);
    assert(floatQueue.rear() == 3.3f);
    assert(floatQueue.size() == 1);

    floatQueue.pop();
    floatQueue.print();
    assert(floatQueue.is_empty());
    assert(floatQueue.size() == 0);
}