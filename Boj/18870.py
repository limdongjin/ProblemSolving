import sys
import bisect
input = sys.stdin.readline

n = int(input())
nums = []
dic1 = {}
i = 0
for _ in input().split():
    nums.append(int(_))
    dic1[i] = int(_)
    i += 1

nums = sorted(set(nums))
ret = ' '.join([str(bisect.bisect_left(nums, dic1[i])) for i in range(n)])

print(ret)