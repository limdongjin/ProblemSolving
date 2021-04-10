import sys
from collections import deque

input = sys.stdin.readline
graph = []
def main():
    n = int(input())
    u, v = [int(_) for _ in input().split()]
    m = int(input())
    global graph
    graph = [[] for i in range(n+1)] # n node
    for _ in range(m):
        a, b = [int(_) for _ in input().split()]
        graph[a].append(b)
        graph[b].append(a)
    print(solve(u, v))


def solve(start, end):
    queue = deque()
    queue.append((start, 0))
    visited = [False for _ in range(len(graph))]
    visited[start] = True
    while queue:
        node, cnt = queue.popleft()
        if node == end:
            return cnt
        for next_node in graph[node]:
            if not visited[next_node]:
                queue.append((next_node, cnt + 1))
                visited[next_node] = True
    return -1


main()