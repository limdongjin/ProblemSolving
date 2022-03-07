import sys
from sys import stdin
from typing import List, Tuple
from collections import namedtuple
from itertools import product

input = stdin.readline
Point = namedtuple('Point', 'y x max')


def possible_large_paper(point: Tuple[int, int], board):
    py, px = point

    end = 5 if max(px, py) + 4 < 10 else 10 - max(px, py)
    cur = 2
    while cur <= end:
        # 열
        if not all(board[y][px + cur - 1] for y in range(py, py + cur)):
            break
        # 행
        if not all(board[py + cur - 1][x] for x in range(px, px + cur)):
            break
        cur += 1
    ret = cur - 1

    return ret


def solve(board: List[List[int]]) -> int:
    points = [(y, x) for y, x in product(range(10), repeat=2) if board[y][x] == 1]
    points_max = [possible_large_paper(point, board) for point in points]
    visited = [[False for _ in range(10)] for _ in range(10)]
    papers = [0]+[5]*5
    ans = sys.maxsize

    def put_paper(idx, size):
        py, px = points[idx]
        is_possible = papers[size] > 0 and all(not visited[y][x]
                                               for y, x in product(range(py, py + size), range(px, px + size)))
        if not is_possible:
            return False
        papers[size] -= 1
        for y, x in product(range(py, py + size), range(px, px + size)):
            visited[y][x] = True
        return True

    def find_next_idx(idx):
        for next_idx in range(idx+1, len(points)):
            y, x = points[next_idx]
            if not visited[y][x]:
                return next_idx
        return -1

    def remove_paper(idx, size):
        py, px = points[idx]
        for y, x in product(range(py, py + size), range(px, px + size)):
            visited[y][x] = False
        papers[size] += 1

    def go(idx, cnt):
        if idx == -1:
            nonlocal ans
            ans = min(ans, cnt)
            return
        for size in range(1, points_max[idx] + 1):
            if not put_paper(idx, size):
                continue
            next_idx = find_next_idx(idx)
            go(next_idx, cnt + 1)
            remove_paper(idx, size)

    if not points_max:
        return 0
    go(0, 0)

    return ans if ans != sys.maxsize else -1

def main():
    board = [list(map(int, input().split())) for _ in range(10)]
    print(solve(board))


if __name__ == '__main__':
    main()
