from sys import stdin
from collections import namedtuple
from typing import List

input = stdin.readline
Point = namedtuple('Point', 'y x')


def cnt_of_invisible(board: List[List[int]], threshold: int):
    def cond(v): return v > threshold
    return sum(cond(val) for row in board for val in row)


def put_paper(board, pos1: Point, pos2: Point):
    # pos1 : left bottom corner
    # pos2 : right top corner
    for y in range(pos1.y, pos2.y + 1):
        for x in range(pos1.x, pos2.x + 1):
            board[y][x] += 1
    return


def main():
    N, M = map(int, input().split())

    # index: 0 ~ 99
    board = [[0 for _ in range(100)] for _ in range(100)]

    for _ in range(N):
        x1, y1, x2, y2 = [int(v) - 1 for v in input().split()]
        put_paper(board, Point(y1, x1), Point(y2, x2))

    print(cnt_of_invisible(board, threshold=M))


main()
