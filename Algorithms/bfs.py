from collections import deque


def link(graph, u, v ):
    graph[u].append(v)


def bfs(graph, vertex):
    queue = deque()
    queue.append(vertex)
    visited[vertex] = True

    while queue:
        cur_node = queue.popleft()
        print(cur_node)
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)


n = 10
graph = {node: [] for node in range(11)}
visited = {node: [] for node in range(11)}

link(graph, 1, 2)
link(graph, 1, 4)

link(graph, 2, 5)
link(graph, 2, 6)

link(graph, 3, 1)
link(graph, 5, 3)
link(graph, 6, 5)

bfs(graph, 1)
