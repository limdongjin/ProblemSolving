def main():
    n = int(input())
    p = list(map(int, input().split()))

    ret = ' '.join(map(str, p)) if prev_perm(p) else -1
    print(ret)


def prev_perm(p):
    n = len(p)

    def swap(i, j):
        p[i], p[j] = p[j], p[i]

    # find i.
    i = n - 1
    while i > 0 and p[i - 1] <= p[i]:
        i -= 1
    if i <= 0:
        return False

    # find j.
    j = n - 1
    while j > 0 and p[j] >= p[i - 1]:
        j -= 1

    swap(j, i - 1)

    # reverse [i, n-1] area
    j = n - 1
    while i < j:
        p[i], p[j] = p[j], p[i]
        i += 1
        j -= 1

    return True


main()
