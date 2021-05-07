


def main():
    while True:
        inp = input()
        if inp == '0':
            break
        S = list(map(int, inp.split()[1:]))
        k = len(S)
        perm = [0]*(k-6)+[1]*6
        ans = []
        while True:
            ans.append([S[i] for i in range(k) if perm[i] == 1])
            if not next_perm(perm):
                break

        ans.sort()
        for a in ans:
            print(' '.join(map(str, a)))
        print()

def next_perm(p):
    def swap(i, j):
        p[i], p[j] = p[j], p[i]
    n = len(p)
    i = n - 1
    while i > 0 and p[i-1]>=p[i]:
        i -= 1
    if i <= 0:
        return False

    j = n - 1
    while p[i-1] >= p[j]:
        j -= 1
    swap(i-1, j)

    j = n - 1
    while i < j:
        swap(i, j)
        i += 1
        j -= 1
    return True
main()
