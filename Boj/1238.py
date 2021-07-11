import sys
import heapq
input = sys.stdin.readline


def dijkstra(from_v):
    dist = [1e9]*(N+1)
    pq = []
    dist[from_v] = 0
    heapq.heappush(pq, (0, from_v))

    while pq:
        cost, v = heapq.heappop(pq)
        cost = cost

        for next_v, next_cost in graph[v]:
            if dist[next_v] > cost + next_cost:
                dist[next_v] = cost+next_cost
                heapq.heappush(pq, (dist[next_v], next_v))
    return dist

N, M, X = map(int, input().split())
graph = {from_v: [] for from_v in range(1, N+1)}

for _ in range(M):
    from_v, to_v, cost = map(int, input().split())
    graph[from_v].append((to_v, cost))


res = [0]*(N+1)
for v in range(1, N+1):
    dist = dijkstra(v)
    res[v] = dist[X]

dist = dijkstra(X)
for v in range(1, N+1):
    res[v] += dist[v]

print(max(res))