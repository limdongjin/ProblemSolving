/*
 * https://programmers.co.kr/learn/courses/30/lessons/42587
 * 문제 제목: 프린터
 */
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cassert>
using namespace std;
class Node {
public:
    int value = -1; // priority
    int idx = -1;
    Node* next = nullptr;
    Node(int value, int idx){
        this->value = value;
        this->idx = idx;
    };
};
class IntQueue {
private:
    int size_ = 0;
    Node* top_ = nullptr;
    Node* bottom_ = nullptr;
public:
    IntQueue(){ }
    IntQueue(int value, int idx){
        this->size_ = 1;
        Node* elem = new Node(value, idx);
        this->top_ = elem;
        this->bottom_ = elem;
    }
    void push(int value, int idx){
        Node* elem = new Node(value, idx);
        Node* topElem = this->top_;
        Node* bottomElem = this->bottom_;
        if(!this->isEmpty()){
            this->top_->next = elem;
            this->top_ = this->top_->next;
        }else{
            this->top_ = elem;
            this->bottom_ = elem;
        }
        this->size_++;
    }
    void pushNode(Node* elem){
        Node* topElem = this->top_;
        Node* bottomElem = this->bottom_;
        if(!this->isEmpty()){
            this->top_->next = elem;
            this->top_ = this->top_->next;
        }else{
            this->top_ = elem;
            this->bottom_ = elem;
        }
        this->size_++;
    }
    int pop(){
        if(this->isEmpty()) throw range_error("queue is empty");
        Node* bottomElem = this->bottom_;
        if(this->size_ == 1){
            this->top_ = nullptr;
            this->bottom_ = nullptr;
        }else{
            this->bottom_ = this->bottom_->next;
        }
        this->size_--;
        return bottomElem->value;
    }
    bool isEmpty(){
        return this->size_ == 0;
    }
    int top(){
        return this->top_->value;
    }
    int bottom(){
        return this->bottom_->value;
    }
    Node* topNode(){
        return this->top_;
    }
    Node* bottomNode(){
        return this->bottom_;
    }
    int size(){
        return this->size_;
    }
};
int solution(vector<int> priorities, int location);
void TestSolution();
void TestIntQueue();

int main(){
    TestIntQueue();
    TestSolution();
}

int solution(vector<int> priorities, int location) {
    int answer = 1, max_priority = 0, i = 0;
    int priorities_map[11] = {0}; // priority 마다 요소가 몇개 있는지 저장.
    int* execute_map = new int[105];
    auto q = new IntQueue();
    for(auto elem : priorities){
        priorities_map[elem] += 1;
        q->push(elem, i);
        if(max_priority < elem) max_priority = elem;
        i++;
    }
    i = 1;
    while(!q->isEmpty()){
        Node* bottomElem = q->bottomNode();
        if(max_priority <= q->bottom()){
            q->pop();
            execute_map[bottomElem->idx] = i;
            priorities_map[max_priority] -= 1;
            if(priorities_map[max_priority] == 0){
                for(int k = max_priority; k >= 0; k--){
                    if(priorities_map[k] > 0){
                        max_priority = k;
                        break;
                    }
                }
            }
            i++;
            continue;
        }
        q->pop();
        q->pushNode(bottomElem);
    }
    return execute_map[location];
}

void TestSolution(){
    vector<int> priorities1{2, 1, 3, 2};
    vector<int> priorities2{1,1,9,1,1,1};

    assert(solution(priorities1, 2) == 1);
    assert(solution(priorities2, 0) == 5);

    cout << "TestSolution Success!" << endl;
}
void TestIntQueue(){
    IntQueue* q = new IntQueue();
    q->push(1, 0);
    assert(q->top() == q->bottom());
    q->push(2, 1);
    q->push(3, 2);

    assert(q->top() == 3);
    assert(q->bottom() == 1);
    q->pop();
    assert(q->top() == 3);
    assert(q->bottom() == 2);
    assert(q->pop() == 2);
    assert(q->size() == 1);
    assert(q->top() == q->bottom());
    printf("TestIntQue Success!");
}