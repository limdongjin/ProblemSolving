class Node:
    def __init__(self, data):
        self.data = data
        self.adj: list[Node] = []
        self.visit = False


def dfs(graph, start_node):
    start_node.visit = True
    [dfs(graph, node)
        for node in start_node.adj
        if not node.visit]


n = int(input())
edge_num = int(input())
graph = [Node(i + 1) for i in range(n)]

for _ in range(edge_num):
    f, s = [int(x) for x in input().split()]
    graph[f - 1].adj.append(graph[s - 1])
    graph[s - 1].adj.append(graph[f - 1])

dfs(graph, graph[0])
print(len([node for node in graph if node.visit]) - 1)
