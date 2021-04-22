import sys


def calculate_diffs(nums):
    ret = 0
    for i in range(len(nums) - 1):
        ret += abs(nums[i] - nums[i + 1])
    return ret


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    ans = calculate_diffs(nums)
    while next_perm(nums):
        ans = max(ans, calculate_diffs(nums))

    print(ans)


def next_perm(p):
    def swap(i, j):
        p[i], p[j] = p[j], p[i]

    n = len(p)

    i = n - 1
    while i > 0 and p[i - 1] >= p[i]:
        i -= 1
    if i <= 0:
        return False

    j = n - 1
    while p[i - 1] >= p[j]:
        j -= 1

    swap(i - 1, j)

    j = n - 1
    while i < j:
        swap(i, j)
        i += 1
        j -= 1
    return True


main()
