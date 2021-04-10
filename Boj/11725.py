from collections import deque
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.adjs = set()

def main():
    n = int(input())
    graph = [Node(i) for i in range(n+1)]
    for i in range(n-1):
        u, v = [int(_) for _ in input().split()]
        graph[u].adjs.add(graph[v])
        graph[v].adjs.add(graph[u])

    bfs(graph[1], n)
    for i in range(2, n+1):
        print(graph[i].parent.id)

def bfs(node, n):
    queue = deque()
    queue.append(node)
    # visited = [False for i in range(n+1) ]
    # visited[node.id] = True
    while queue:
        cur_node = queue.popleft()

        for next_node in cur_node.adjs:
            next_node.parent = cur_node
            queue.append(next_node)
            next_node.adjs.remove(cur_node)
            # visited[next_node.id] = True

main()