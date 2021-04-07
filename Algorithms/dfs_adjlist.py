from typing import List, Dict


# u -> v 를 연결한다.
def link(graph: Dict, u: int, v: int):
    graph[u].append(v)


def dfs(graph: Dict, visited: Dict, vertex: int):
    visited[vertex] = True
    print(vertex)
    for next_node in graph[vertex]:
        if not visited[next_node]:
            dfs(graph=graph, visited=visited, vertex=next_node)


def dfs_stack(graph: Dict, visited: Dict, vertex: int):
    stack =[]
    stack.append(vertex)
    print(vertex)

    while stack:
        cur_node = stack[-1]
        visited[cur_node] = True

        for next_node in graph[cur_node]:
            if not visited[next_node]:
                print(next_node)
                stack.append(next_node)
                break

        if cur_node == stack[-1]:
            stack.pop()


n = 10
graph: Dict = {i: [] for i in range(n + 1)}
visited = {i: False for i in range(n+1)}

link(graph=graph, u=1, v=2)
link(graph=graph, u=2, v=5)
link(graph=graph, u=2, v=1)
link(graph=graph, u=2, v=3)
link(graph=graph, u=3, v=2)
link(graph=graph, u=3, v=5)


print("============= recursive dfs ===========")
dfs(graph=graph, visited=visited, vertex=1)

print()
print("============= stack dfs ===========")
visited = {i: False for i in range(n+1)}
dfs_stack(graph=graph, visited=visited, vertex=1)
