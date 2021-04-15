from collections import deque
import sys
from enum import Enum


class Op(Enum):
    ROOT = -1
    D = 1
    S = 2
    L = 3
    R = 4


def main():
    input = sys.stdin.readline
    tc = int(input())
    for _ in range(tc):
        a, b = [int(_) for _ in input().split()]

        print(solve(a, b))


def solve(a, b):
    queue = deque()

    # 경로를 역추적하기위한 딕셔너리
    # { to: (from, op) } 형태
    # ex, {16: (8, Op.D)} 는 8 에서 D 연산으로 16이 되었다는것
    dic = {a: (-1, Op.ROOT)}

    # 경로의 길이 및 방문했는지 저장
    d = [-1 for _ in range(10001)]

    queue.append(a)
    d[a] = 0

    while queue:
        num = queue.popleft()

        for op in [Op.D, Op.S, Op.L, Op.R]:
            v = op_execute(num, op)

            if v == b:
                dic[v] = (num, op)
                return get_history(dic, b)

            # 최초 방문했거나, 더 짧은 경로인 경우
            if d[v] == -1 or d[v] > d[num] + 1:
                d[v] = d[num] + 1
                dic[v] = (num, op)
                queue.append(v)


def op_execute(num, op):
    op_d = lambda: (num * 2) % 10000
    op_s = lambda: num - 1 if num != 0 else 9999
    op_l = lambda: (num % 1000) * 10 + num // 1000
    op_r = lambda: (num % 10) * 1000 + num // 10

    op_map = {Op.D: op_d, Op.S: op_s, Op.L: op_l, Op.R: op_r}

    return op_map[op]()


def get_history(dic, dest):
    ret = []
    cur = dest

    while cur != -1:
        op = dic[cur][1]
        if op == Op.ROOT:
            break
        ret.append(op.name)
        cur = dic[cur][0]

    ret.reverse()

    return ''.join(ret)


main()
