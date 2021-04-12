# 4.6 후속자
def main():
    # test_make_bst()
    numbers = [0, 10, 15, 20, 25, 30, 31, 34]
    root: Node = list_to_bst(numbers)

    # Given some node
    # 0 이 현재 노드이다.
    current_node: Node = root.left.left

    # 후속자 노드가 잘 뽑히는 것을 확인할수있다.
    assert current_node.data == numbers[0]
    print('first node ', current_node.data)
    for idx in range(1, len(numbers)):
        next_node = inorder_succ(current_node)
        print('next_node ', next_node.data)

        assert next_node.data == numbers[idx]
        current_node = next_node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


def list_to_bst(sorted_list):
    return _make_bst(sorted_list, 0, len(sorted_list) - 1)


def _make_bst(list, start, end):
    root_idx = start + (end - start)//2
    if start > end:
        return None
    if start == end:
        return Node(list[start])

    root = Node(list[root_idx])
    root.left = _make_bst(list, start, root_idx - 1)

    if root.left is not None:
        root.left.parent = root

    root.right = _make_bst(list, root_idx + 1, end)
    if root.right is not None:
        root.right.parent = root

    return root

def test_make_bst():
    list = [1,2,3,4,5,6,7,9,10]
    root = list_to_bst(list)

    assert root.left.data <= root.data <= root.right.data
    assert root.left.left.data <= root.left.data <= root.left.right.data


def inorder_succ(node):
    if node.right:
        return leftest_node(node.right)
    else:
        cur_node = node
        while cur_node == cur_node.parent.right:
            cur_node = cur_node.parent
        return cur_node.parent

def leftest_node(node):

    cur_node = node
    while cur_node.left:
        cur_node = cur_node.left
    return cur_node

# Given BST


