/*
 * https://programmers.co.kr/learn/courses/30/lessons/42585
*  문제 제목: 쇠막대기
*/
#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
#include <cassert>

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
//        if(this->isEmpty()) throw range_error("stack is empty");
        return this->top_->value;
    }
    int pop(){
//        if(this->isEmpty()) throw range_error("stack is empty");
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
int solution(string arrangement);
void TestSolution();
int main(){
    TestSolution();
}

int solution(string arrangement){
    int answer = 0;
    auto openBrackets = new IntStack();
    int idx = 0;
    int flag = 0;
    for(char c : arrangement){
        if(c == '(' && flag == 0){
            flag = 1;
        }else if(c == '('){
            // 이전 (가 막대의 (를 의미하는 조건.
            openBrackets->push(idx - 1);
        }else if(c == ')' && flag == 1){
            // 레이저 조건.
            answer += openBrackets->size();
            flag = 0;
        }else if(c == ')'){
            // 막대가 닫히는 경우
            answer += 1;
            openBrackets->pop();
        }
        idx++;
    }
    return answer;
}
void TestSolution(){
    string s1 = "()(((()())(())()))(())";
    assert(solution(s1) == 17);
    cout << "pass " << s1 << " " << 17 << endl;

    cout << "Test Success!" << endl;
}