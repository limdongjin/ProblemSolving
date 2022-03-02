from sys import stdin
from collections import namedtuple, deque
from typing import List
input = stdin.readline
Point = namedtuple('Point', 'x y id')


def dist(pos1: Point, pos2: Point):
    return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)

def make_adj_table(nodes: List[Point]):
    n = len(nodes)
    adj = [[False]*n for _ in range(n)]

    for s1 in range(n-1):
        for s2 in range(s1, n):
            if dist(nodes[s1], nodes[s2]) <= 1000:
                adj[s1][s2] = True
                adj[s2][s1] = True
    return adj

def solve(home: Point, shops: List[Point], fest: Point) -> str:
    def bfs():
        q: deque[int] = deque()
        visited = [False]*(snum+1)
        q.append(0)  # home(=0) 에서 출발

        while q:
            cur = q.popleft()
            if adj[cur][fest_id]:
                # cur 노드와 페스티벌(=n+1) 노드를 잇는 간선이 있는가?
                return 'happy'

            for next_shop in range(1, snum+1):
                if not adj[cur][next_shop] or visited[next_shop]:
                    continue
                # 인접한 shop 노드를 큐에 삽입
                q.append(next_shop)
                visited[next_shop] = True
        return 'sad'

    snum = len(shops)
    fest_id = snum + 1

    nodes = [home, *shops, fest]
    # 0번노드=home, 1 ~ snum :shops, snum+1번노드=fest

    adj = make_adj_table(nodes)
    ret = bfs()

    return ret


def main():
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        home = Point(*map(int, input().split()), 0)
        shops = [Point(*map(int, input().split()), i+1) for i in range(n)]
        fest = Point(*map(int, input().split()), n+1)

        print(solve(home, shops, fest))


if __name__ == '__main__':
    main()
