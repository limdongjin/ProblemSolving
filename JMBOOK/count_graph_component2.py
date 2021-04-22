
def main():
    graph = [[1, 2], [0], [1,2], [4], [5], [], []]
    v_len = len(graph)
    visited = [False for v in range(v_len)]
    cnt = 0
    for i in range(v_len):
        if not visited[i]:
            cnt = cnt + 1
            dfs(graph, visited, i)
    print(cnt)


def dfs(graph, visited, node_id):
    visited[node_id] = True
    for adj in graph[node_id]:
        if not visited[adj]:
            dfs(graph, visited, adj)

main()