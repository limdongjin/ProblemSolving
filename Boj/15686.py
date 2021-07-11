from itertools import combinations, product
from sys import stdin

input = stdin.readline


# 좌표 p1 과 p2 가 주어졌을때, 두 좌표간 거리를 구한다.
def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def minChickDist(chicks, house):
    return min(dist(chick, house)
               for chick in chicks)


# @param c : (폐업하지않은)치킨 리스트
# @param h : 집 리스트
# @return 도시의 치킨 거리
def cityChickDist(chicks, houses) -> int:
    return sum(minChickDist(chicks, house)
               for house in houses)


def main():
    n, m = map(int, input().split())
    board = [input().rstrip().split()
             for _ in range(n)]
    houses = [(y, x)
              for y, x in product(range(n), range(n))
              if board[y][x] == '1']

    chicks = [(y, x)
              for y, x in product(range(n), range(n))
              if board[y][x] == '2']

    ans = min(cityChickDist(selected_chicks, houses)
              for selected_chicks in combinations(chicks, m))

    print(ans)


main()
