from collections import deque

# very easy topological sort problem

N, M = map(int, input().split())
indegree = [0]*(N+1)
graph = {v: [] for v in range(1, N+1)}

for _ in range(M):
    l, r = map(int, input().split())
    graph[l].append(r)
    indegree[r] += 1

# indegree 가 0 인 애들부터 큐에 넣는다.
q = deque([v for v in range(1, N+1) if indegree[v] == 0])

ans = []
while q:
    v = q.pop()
    ans.append(v)

    for adj_v in graph[v]:
        # v 는 제거되었으므로 adj_v 의 indegree 가 1줄어든다.
        indegree[adj_v] -= 1
        if indegree[adj_v] == 0:
            # indegree 가 0이 되면 큐에 넣는다.
            q.append(adj_v)

print(' '.join(map(str, ans)))
