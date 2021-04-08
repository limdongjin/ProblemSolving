
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def copy_bst_to_list(root: Node):
    if root is None:
        return []
    left = copy_bst_to_list(root.left)
    right = copy_bst_to_list(root.right)

    ret = []
    ret.extend(left)
    ret.append(root)
    ret.extend(right)

    return ret


root = Node(5)
root.left = Node(4)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4.5)
root.right.left = Node(6)
root.right.right = Node(8)

list = copy_bst_to_list(root)
for v in list:
    print(v.data, end=' ')

# BST 를 중위 순회하면 정렬된 리스트가 나와야한다.
prev = -100
for num in list:
    assert prev <= num.data
    prev = num.data