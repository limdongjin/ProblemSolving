#include <cstdio>
#include <typeinfo>

template <class T>
class ArrayStack{

public:
    ArrayStack(int max_size){
        stack_ = new T [max_size];
        size_ = 0;
    }
    int getSize(){
        return size_;
    }
    const char* getTypeOfElements(){
        return typeid(T).name();
    }
    T get(){
        try{
            if(!(size_)) throw size_;
            return stack_[size_ - 1];
        }catch(int exec){
            if(!(exec)) printf("Stack is Empty!\n");
            exit(1);
        }
    }
    void push(T new_data){
        stack_[size_] = new_data;
        size_ = size_ + 1;
    }
    T pop(){
        T res = stack_[size_ - 1];
        size_ = size_ - 1;
        
        return res;
    }
    
private:
    int size_;
    T* stack_;
    
};

int main(void){
    printf("It is Stack Implementation\n");
    
    ArrayStack<float> array_stack = ArrayStack<float>(100);
    
    printf("%d\n", array_stack.getSize());
    printf("%s\n", array_stack.getTypeOfElements());
    
    array_stack.push(0.1);
    array_stack.pop();
    
    printf("\n%f\n", array_stack.get());
}
