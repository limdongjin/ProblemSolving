import itertools
import sys
input = sys.stdin.readline 
def main():
    n = int(input())
    nums = [int(_) for _ in input().split()]
    ret = -1
    for perm in itertools.permutations(nums):
        ret = max(ret, calculate(perm))
    print(ret)
def calculate(a):
    ret = 0
    for i in range(len(a) - 1):
        ret += abs(a[i] - a[i+1])
    return ret
main()
