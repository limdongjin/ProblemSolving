import sys
import itertools
input = sys.stdin.readline


def solve(a: str, b: str) -> int:
    a = ''.join(sorted(a, reverse=True))
    ret = -1
    for c in itertools.permutations(a):
        if c[0] == '0': continue
        candidate = int(''.join(c))
        if candidate < int(b):
            ret = candidate
            break

    return ret


if __name__ == '__main__':
    # test start
    assert solve('1', '2') == 1
    assert solve('4', '40') == 4
    assert solve('98', '500') == 98
    assert solve('9820', '9810') == 9802
    assert solve('900', '555') == -1
    assert solve('444', '444') == -1
    assert solve('4603', '3456') == 3406
    assert solve('9000', '9999') == 9000
    assert solve('1234', '3456') == 3421
    assert solve('1000', '5') == -1
    assert solve('789', '123') == -1
    # test end

    A, B = input().split()
    print(solve(A, B))
