


def main():
    n = int(input())
    p = list(map(int, input().split()))

    ret = ' '.join(map(str, p)) if next_perm(p) else -1
    print(ret)

def next_perm(p):
    n = len(p)

    # find i
    i = n - 1
    while i > 0 and p[i-1] >= p[i]:
        i -= 1
    if i <= 0:
        return False

    # find j
    j = n - 1
    while p[j] <= p[i-1]:
        j -= 1

    # swap
    p[i-1], p[j] = p[j], p[i-1]

    # reverse
    j = n - 1
    while i < j:
        p[i], p[j] = p[j], p[i]
        i += 1
        j -= 1

    return True

main()