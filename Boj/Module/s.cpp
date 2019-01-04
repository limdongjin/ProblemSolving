#include <iostream>
#include <stack>

int main(void){
    std::stack<int> mska;
    try{
        std::cout << (mska.top());
    }catch(int){
        printf("error");
    }   
}
