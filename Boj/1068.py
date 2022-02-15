import sys
sys.setrecursionlimit(200000000)
input = sys.stdin.readline


class Node:
    def __init__(self, id):
        self.id = id
        self.childs = []


def main():
    n = int(input())
    nodes = [Node(int(_)) for _ in range(n)]
    s = input().split()
    root_idx = 0
    for i in range(n):
        p = int(s[i])
        if p == -1:
            root_idx = i
            continue
        nodes[p].childs.append(nodes[i])

    target = int(input())
    if target == root_idx:
        print(0)
        exit()

    cache = [-1 for _ in range(n)]
    dfs(node=nodes[root_idx], cache=cache, target=target)

    print(cache[root_idx])


def dfs(node, cache, target):

    # 자식노드가 없다는 것은 리프노드라는 것
    if not node.childs:
        cache[node.id] = 1
        return
    # 자식노드가 하나이면서 그 자식이 타겟이라는것은, 이 자식을 제거하면 자신이 리프노드가 된다는 것
    if len(node.childs) == 1 and node.childs[0].id == target:
        cache[node.id] = 1
        return

    ret = 0
    for child in node.childs:
        if child.id == target:
            cache[child.id] = 0
            continue
        if cache[child.id] == -1:
            dfs(node=child, cache=cache, target=target)
            ret += cache[child.id]

    cache[node.id] = ret
    return


main()
