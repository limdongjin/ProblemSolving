from sys import stdin
from collections import namedtuple
from typing import List
import sys
sys.setrecursionlimit(300001)

input = stdin.readline
Jewel = namedtuple('Jewel', 'weight price')


class Node:
    def __init__(self, d):
        self.d = d
        self.l = None
        self.r = None


def array_to_bst(arr: List[int]) -> Node:
    arr.sort()
    def _to_bst(nums):
        if not nums:
            return None
        mid = len(nums)//2
        root = Node(nums[mid])
        root.l = _to_bst(nums[:mid])
        root.r = _to_bst(nums[mid+1:])
        return root

    return _to_bst(arr)

def solve(jewels: List[Jewel], bags: List[int]) -> int:
    ret = 0
    jewels.sort(key=lambda jew: jew.price + jew.weight)
    root = array_to_bst(bags)

    for jewel in jewels:
        # find bag
        

    assert False


def test():
    bst_root = array_to_bst([1, 2, 3, 4, 5, 6, 7, 8])
    print(bst_root.l.d)


def main():
    n, k = map(int, input().split())
    jewels = [Jewel(*map(int, input().split())) for _ in range(n)]
    bags = [int(input()) for _ in range(k)]

    print(solve(jewels, bags))


if __name__ == '__main__':
    test()
    # main()
