from typing import List


def dfs(adj_matrix: List[List[bool]], visited: List[bool], vertex: int):
    visited[vertex] = True  # 방문 처리 한다
    print(vertex)
    for next_node, is_adj in enumerate(adj_matrix[vertex]):
        if is_adj and not visited[next_node]: # 인접 and 미방문 이라면 dfs 를 호출
            dfs(adj_matrix=adj_matrix, visited=visited, vertex=next_node)


def dfs_stack(adj_matrix: List[List[bool]], visited: List[bool], vertex: int):
    stack = []
    print(vertex)
    stack.append(vertex)
    while stack:
        cur_node = stack[-1]
        visited[cur_node] = True

        for next_node, is_adj in enumerate(adj_matrix[cur_node]):
            if is_adj and not visited[next_node]:
                print(next_node)
                stack.append(next_node)
                break  # break 을 하는 이유는, dfs 특성상 인접 정점이 나오면 바로 진입하기때문임.

        if cur_node == stack[-1]:  # 인접 정점이 없는 경우 이전 정점으로 돌아가기 위함이다.
            stack.pop()


n = 10  # 정점의 개수

# adj[n + 1][n + 1]
# u 와 v 가 연결되었다면 adj_matrix[u][v] == True
# 인접 행렬이며, 0 인덱스는 사용하지않는다.
adj_matrix = [[False] * (n + 1) for _ in range(n + 1)]

# 방문 여부를 저장하는 리스트
# visited[u] 가 True 라면 u 정점이 방문 되었다는 것을 의미함.
visited = [False] * (n + 1)

# 1 - 2 - 3 - 4
#   - 6
adj_matrix[1][2] = True
adj_matrix[1][6] = True
adj_matrix[2][3] = True
adj_matrix[3][4] = True
adj_matrix[4][1] = True

print("============= recursive dfs ===========")
dfs(adj_matrix=adj_matrix, visited=visited, vertex=1)

print()
print("============= stack dfs ===========")
visited = [False] * (n + 1)
dfs_stack(adj_matrix=adj_matrix, visited=visited, vertex=1)
