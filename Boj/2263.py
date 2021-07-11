import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

class Node:
    def __init__(self, v, l, r):
        self.v = v
        self.left = l
        self.right = r

def build_tree(istart, iend, pstart, pend):
    if istart > iend:
        return None
    if pstart > pend:
        return None
    # 병목 지점
    # root_idx = inorder.index(postorder[pend], istart, iend+1)
    # index 와 값을 매핑한 테이블을 만들자!
    root_idx = idx_table[postorder[pend]]

    root = Node(inorder[root_idx], None, None)
    if istart == iend:
        return root

    # 병목지점2
    # 처음에는 slice로 구현했었는데, 메모리 초과가 났다.
    # 그래서 시작,끝 인덱스를 전달하도록 변경
    root.left = build_tree(istart, root_idx-1, pstart, pstart+(root_idx-istart)-1)
    root.right = build_tree(root_idx+1, iend, pstart+(root_idx-istart), pend-1)

    return root

def preorder(root):
    if not root:
        return
    global ans
    ans += str(root.v) + ' '
    preorder(root.left)
    preorder(root.right)


N = int(input())
inorder = [int(_) for _ in input().split()]
postorder = [int(_) for _ in input().split()]
idx_table = {v: i for i, v in enumerate(inorder)}
root = build_tree(0, len(inorder)-1, 0, len(postorder)-1)

ans = ''
preorder(root)
print(ans)