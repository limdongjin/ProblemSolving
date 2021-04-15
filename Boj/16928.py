from collections import deque
import sys
input = sys.stdin.readline

def main():
    N, M = [int(_) for _ in input().split()]
    jump = [-1 for _ in range(101)]

    for i in range(N+M):
        f, to = [int(_) for _ in input().split()]
        jump[f] = to

    print(solve(jump))

def solve(jump):

    return bfs(1, jump)


def bfs(pos, jump):
    dd = [-1 for _ in range(101)]
    dd[1] = 0
    queue = deque()
    queue.append(pos)

    while queue:
        x = queue.popleft()

        for dx in range(1, 7):
            nx = x + dx
            if nx > 100:
                continue
            if jump[nx] != -1:
                nx = jump[nx]
            if dd[nx] == -1:
                dd[nx] = dd[x] + 1
                queue.append(nx)

    return dd[100]

main()
