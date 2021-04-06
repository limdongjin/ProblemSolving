import sys
input = sys.stdin.readline
sys.setrecursionlimit(2500*2500)

class Graph:
    def __init__(self):
        self.nodes = []
    def add_edge(self, u, v):
        node1 = self.nodes[u-1]
        node2 = self.nodes[v-1]
        node1.adjs.append(node2)
        node2.adjs.append(node1)

class Node:
    def __init__(self, data):
        self.data = data
        self.adjs = []
        self.visited = False

def dfs(node: Node):
    for nde in node.adjs:
        if nde.visited:
            continue
        nde.visited = True
        dfs(nde)

N, M = [int(x) for x in input().split()]
graph = Graph()
for _ in range(N):
    graph.nodes.append(Node(_))
for _ in range(M):
    u, v = [int(x) for x in input().split()]
    graph.add_edge(u, v)

ret = 0
for node in graph.nodes:
    if node.visited:
        continue
    node.visited = True
    ret = ret + 1
    dfs(node)

print(ret)