import sys
input = sys.stdin.readline
class Node:
    def __init__(self, v):
        self.v = v
        self.next =None
        self.prev =None

def linkedlist(n):
    head = Node(1)
    cur = head
    for i in range(2, n+1):
        nnode = Node(i)
        cur.next = nnode
        nnode.prev = cur
        cur = cur.next
    
    head.prev = cur    
    cur.next = head
    
    return head

def print_node(head):
    cur = head
    while cur:
        print(cur.v, end=' ')
        cur = cur.next
        if cur == head:
            break
    print()

def remove_node(node):
    node.prev.next = node.next
    node.next.prev = node.prev
    ret = node.next
    return ret

for _ in range(int(input())):
    N, K = map(int, input().split())
    # head node
    L = linkedlist(N)
    cur_n = N
    cur = L
    while cur:
        if cur.next.next == cur:
            break
        cur = remove_node(cur)
        cur_n -= 1
        # move
        for i in range((K-1)%cur_n):
            cur = cur.next
    if cur.v > cur.next.v:
        print(cur.next.v, cur.v)
    else:
        print(cur.v, cur.next.v)
