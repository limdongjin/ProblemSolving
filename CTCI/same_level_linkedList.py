# 4.3 problem
from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def solve(root: Node):
    ret = []
    queue = deque()
    queue.append(root)

    while queue:
        size = len(queue)
        linkedlist = []
        for _ in range(size):
            node = queue.popleft()
            linkedlist.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ret.append(linkedlist)
    return ret
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)

root.left.left.left = Node(9)

linked_lists = solve(root)
for list in linked_lists:
    for v in list:
        print(v, end=' ')
    print()