#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

#define swap(a, b, typ) do { typ t; t = (a); (a) = (b); (b) = t; } while(0)
using namespace std;

void swim(vector<int>& heap, size_t k){
    while (k > 0 && heap[(k-1)/2] < heap[k]){
        swap(heap[(k-1)/2], heap[k], int);
        k = (k-1)/2;
    }
}

void sink(vector<int>& heap, size_t k){
    size_t here = k;

    while(true){
        int left = here*2 + 1, right = here*2 + 2;

        if (left >= heap.size()) break;
        int next = here;

        if (heap[next] < heap[left]) next = left;
        if (right < heap.size() && heap[next] < heap[right]) next = right;

        if (next == here) break;
        swap(heap[here], heap[next], int);
        here = next;
    }
}

// jmbook p728
void push_heap(vector<int>& heap, int newValue){
    heap.push_back(newValue);

    // my code
    swim(heap, heap.size()-1);

//    original code
//    int idx = heap.size() - 1;
//
//    while(idx > 0 && heap[(idx-1)/2] < heap[idx]){
//        swap(heap[idx], heap[(idx-1)/2], int);
//        idx = (idx-1)/2;
//    }
}

// jmbook p730
void pop_heap(vector<int>& heap){
    heap[0] = heap.back();
    heap.pop_back();

// my code
    sink(heap, 0);

//    original code
//    int here = 0;
//    while(true){
//        int left = here*2 + 1, right = here*2 + 2;
//
//        if (left >= heap.size()) break;
//        int next = here;
//
//        if (heap[next] < heap[left]) next = left;
//        if (right < heap.size() && heap[next] < heap[right]) next = right;
//
//        if (next == here) break;
//        swap(heap[here], heap[next], int);
//        here = next;
//    }

}

void print_heap(vector<int> heap){
    for (const auto &item : heap)
        cout << item << ";";
    cout << endl;
}

int main(){
    cout << "hello world" << endl;
    vector<int> heap;
   
    push_heap(heap, 10);
    push_heap(heap, 20);
    push_heap(heap, -29);
    pop_heap(heap); // pop 20
    push_heap(heap, 300);
    pop_heap(heap); // pop 300

    print_heap(heap); // 10;-29;
}

