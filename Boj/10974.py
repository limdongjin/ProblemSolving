


def main():
    n = int(input())
    nums = list(range(1, n+1))
    print_ans = lambda a: print(' '.join(map(str, a)))

    print_ans(nums)

    while next_perm(nums):
        print_ans(nums)


def next_perm(p):
    def swap(i, j):
        p[i], p[j] = p[j], p[i]
    n = len(p)

    i = n - 1
    while i > 0 and p[i-1] >= p[i]:
        i -= 1
    if i <= 0:
        return False

    j = n - 1
    while j > 0 and p[i-1] >= p[j]:
        j -= 1

    swap(i-1, j)

    j = n - 1
    while i < j:
        swap(i, j)
        i += 1
        j -= 1

    return True
main()