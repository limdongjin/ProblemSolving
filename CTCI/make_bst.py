import sys
from collections import deque
sys.setrecursionlimit(100000000)


class Node:
    def __init__(self, id, left=None, right=None):
        self.id = id
        self.left = left
        self.right = right


def make_bst(numbers, start, end):
    size = end - start + 1
    root_idx = start + size//2
    # print(start, end, root_idx, size)
    if end < start:
        return None
    if size == 1:
        return Node(numbers[root_idx])

    root = Node(numbers[root_idx])
    root.left = make_bst(numbers, start, root_idx - 1)
    root.right = make_bst(numbers, root_idx + 1, end)

    return root

def simple_print(node):
    queue = deque()
    queue.append(node)
    level = 1
    while queue:
        size = len(queue)
        for i in range(size):
            cur_node = queue.popleft()
            print(cur_node.id, end=' ')
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        print()
        level = level+1


sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
start = 0
end = len(sorted_numbers) - 1
root = make_bst(sorted_numbers, start, end)

simple_print(root)

assert root.id == 5
assert root.left.id == 3
assert root.right.id == 7

assert root.left.left.id == 2
assert root.left.right.id == 4

assert root.right.left.id == 6
assert root.right.right.id == 8

assert root.left.left.left.id == 1