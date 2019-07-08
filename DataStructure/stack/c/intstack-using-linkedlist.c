#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef struct _node {
    int data;
    struct _node* next;
} Node;

typedef struct _stack {
    Node* top;
    int size;
} Stack;

Node* construct_node_with(int data, Node* link);
void destroy_node(Node** node);

Stack* construct_stack();
void destroy_stack(Stack** stack);
void push_in_stack(Stack* stack, int data);
void pop_in_stack(Stack* stack);
void print_stack(Stack* stack);
int top_data_in_stack(Stack* stack);

int main(){
    Stack* stack = construct_stack();
    push_in_stack(stack, 1);
    push_in_stack(stack, 2);
    push_in_stack(stack, 3);
    push_in_stack(stack, 1);
    push_in_stack(stack, 1);

    print_stack(stack);
    pop_in_stack(stack);

    print_stack(stack);
    print_stack(stack);

    pop_in_stack(stack);
    print_stack(stack);

    pop_in_stack(stack);
    print_stack(stack);

    top_data_in_stack(stack);
    destroy_stack(&stack);
}


Node* construct_node_with(int data, Node* link){
    Node* node = (Node*)malloc(sizeof(Node));
    node->data = data;
    node->next = link;

    return node;
}

void destroy_node(Node** node){
    (*node)->next = NULL;
    free(*node);
    *node = NULL;
}


Stack* construct_stack(){
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    stack->top = NULL;
    stack->size = 0;

    return stack;
}

void destroy_stack(Stack** stack){
    assert(stack);

    Node* node = (*stack)->top;
    Node* tmp;
    while(node != NULL){
        tmp = node->next;
        destroy_node(&node);
        node = tmp;
    }

    (*stack)->size = 0;
    free(*stack);
    (*stack)->top = NULL;
    *stack = NULL;

    return;
}

void push_in_stack(Stack* stack, int data){
    assert(stack);

    stack->size++;
    Node* node = construct_node_with(data, stack->top);
    stack->top = node;
}

void pop_in_stack(Stack* stack){
    assert(stack);
    assert(stack->size != 0);

    stack->size--;
    Node* node = stack->top;
    stack->top = node->next;
}

void print_stack(Stack* stack){
    assert(stack);

    Node* tmp = stack->top;
    printf("top ");
    while(tmp != NULL){
        printf("%d ", tmp->data);
        tmp = tmp->next;
    }
    printf("bottom\n");
}

int top_data_in_stack(Stack* stack){
    assert(stack);
    assert(stack->top);

    printf("%d\n", stack->top->data);
}
