import sys
input = sys.stdin.readline

def next_permutation(a):
    n = len(a)
    # find i
    i = n - 1
    while i > 0 and not(a[i-1] < a[i]):
        i -= 1
    if i == 0:
        return False

    # find j
    j = n - 1
    while j > 0 and not(a[i-1] < a[j]):
        j -= 1

    # swap
    a[i-1], a[j] = a[j], a[i-1]

    # reverse inplace
    k = n - 1
    while i < k:
        a[i], a[k] = a[k], a[i]
        i += 1
        k -= 1

    return True

def sum_(nums, select):
    return sum(nums[i] for i in range(0, len(nums)) if select[i])

N, S = map(int, input().split())
nums = [int(_) for _ in input().split()]
ret = 0

for size in range(1, N+1):
    select = [0]*(N-size) + [1]*size
    if sum_(nums, select) == S:
        ret += 1
    while next_permutation(select):
        if sum_(nums, select) == S:
            ret += 1

print(ret)
