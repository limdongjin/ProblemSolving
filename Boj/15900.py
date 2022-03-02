import sys
from typing import List

input = sys.stdin.readline

tree: List[List[int]]
sum_depth: int
visited: List[bool]


def dfs(node, count):
    global tree, sum_depth, visited
    stack = [(node, count)]
    while stack:
        v, cnt = stack.pop()
        visited[v] = True
        if len(tree[v]) == 1 and v != 1:
            sum_depth += cnt
            continue
        stack.extend([(next_node, cnt + 1)
                      for next_node in tree[v] if not visited[next_node]])


if __name__ == '__main__':
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    visited = [False] * (n + 1)  # 1 ~ n
    visited[1] = True
    sum_depth = 0
    dfs(1, 0)
    print('Yes' if sum_depth % 2 else 'No')
