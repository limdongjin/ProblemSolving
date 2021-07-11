import sys
input = sys.stdin.readline

def dfs(v, cost):
    global far_v, dist
    if visited[v]:
        return
    if cost > dist:
        dist = cost
        far_v = v

    visited[v] = True
    for adj_v, c in graph[v]:
        if not visited[adj_v]:
            dfs(adj_v, cost+c)
    return

V = int(input())

# graph[from] = [(to, cost), (to2, cost2)]
graph = {from_v: [] for from_v in range(1, V+1)}
ans = float('-inf')

for _ in range(V):
    line = list(map(int, input().split()))
    from_v = line[0]
    for i in range(1, len(line)-1, 2):
        graph[from_v].append((line[i], line[i+1]))

far_v, dist = -1, -1

visited = [False]*(V+1)
dfs(1, 0)

visited = [False]*(V+1)
dfs(far_v, 0)

print(dist)
