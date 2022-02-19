from sys import stdin
import heapq

input = stdin.readline


def solve(V, E, adj, v1, v2):
    def dijkstra(src):
        dist = [float('inf') for _ in range(V)]
        dist[src] = 0
        pq = []
        heapq.heappush(pq, (dist[src], src))

        while pq:
            cost, here = heapq.heappop(pq)
            if dist[here] < cost:
                continue
            for there in range(V):
                weight = adj[here][there]
                if weight == 1404:
                    continue
                next_dist = cost + weight
                if dist[there] > next_dist:
                    dist[there] = next_dist
                    heapq.heappush(pq, (next_dist, there))

        return dist

    dist_to = dijkstra(0)
    if float('inf') in (dist_to[v1], dist_to[v2], dist_to[V - 1]):
        return -1

    path1 = dist_to[v1]
    path2 = dist_to[v2]

    dist_to = dijkstra(v1)
    path1 += dist_to[v2]
    path2 += dist_to[V - 1]

    dist_to = dijkstra(v2)
    path1 += dist_to[V - 1]  # 0->v1->v2->V-1
    path2 += dist_to[v1]     # 0->v2->v1->V-1

    return min(path1, path2)


def main():
    V, E = map(int, input().split())
    adj = [[1404 for _ in range(V)] for _ in range(V)]

    for _ in range(E):
        a, b, c = map(int, input().split())
        if c < adj[a - 1][b - 1]:
            adj[a - 1][b - 1] = adj[b - 1][a - 1] = c
    v1, v2 = [int(x) - 1 for x in input().split()]

    res = solve(V, E, adj, v1, v2)

    print(res)


main()
