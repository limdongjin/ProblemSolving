from collections import deque
import sys
input = sys.stdin.readline

def main():
    N, M = [int(_) for _ in input().split()]
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = [int(_) for _ in input().split()]
        graph[u].append(v)
        graph[v].append(u)

    solve(graph, N)

def solve(graph, N):
    scores = [0 for i in range(N+1)]
    for node in range(1, N+1):
        scores[node] = run_game(graph, node)

    # print(scores)
    prev = (-1, 10000)
    for node in range(1, N+1):
        if scores[node] < prev[1]:
            prev = (node, scores[node])
    print(prev[0])

def run_game(graph, node):
    queue = deque()
    visited = [0 for _ in range(len(graph))]
    queue.append(node)
    visited[node] = 1

    level = 0
    while queue:
        size = len(queue)
        level += 1
        for _ in range(size):
            cur = queue.popleft()
            for next_node in graph[cur]:
                if visited[next_node] == 0:
                    queue.append(next_node)
                    visited[next_node] = level
    # print(level)
    # print(node, visited)
    return sum(visited) - 1

main()