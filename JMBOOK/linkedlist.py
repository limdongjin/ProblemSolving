

class ListNode:
    def __init__(self):
        self.v = None
        self.next = None
        self.prev = None
    

def delete_node(node):
    node.prev.next = node.next
    node.next.prev = node.prev

def recover_node(node):
    node.prev.next = node
    node.next.prev = node

def print_node(head):
    cur = head
    while cur:
        print(cur.v, end=' ')
        cur = cur.next
    print()
def print_reverse_node(tail):
    cur = tail
    while cur:
        print(cur.v, end=' ')
        cur = cur.prev
    print()

node1 = ListNode()
node2 = ListNode()
node3 = ListNode()
node1.v, node2.v, node3.v = 1, 2, 3
node1.next, node2.prev, node2.next, node3.prev = node2, node1, node3, node2

print_node(node1)
print_reverse_node(node3)

print('delete 2')
delete_node(node2)
print_node(node1)
print_reverse_node(node3)

print('recover 2')
recover_node(node2)
print_node(node1)

