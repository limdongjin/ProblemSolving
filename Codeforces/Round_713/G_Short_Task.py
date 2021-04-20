
def main():
    t = int(input())
    MAX_C = 10**7 + 99
    d = [-1 for _ in range(MAX_C)]
    s = [0 for _ in range(MAX_C)]
    ans = [-1 for _ in range(MAX_C)]

    # fill
    for i in range(2, MAX_C):
        if i*i >= MAX_C:
            break
        if d[i] == -1:
            d[i] = i
            for j in range(i*i, MAX_C, i):
                if d[j] == -1:
                    d[j] = i

    s[1] = 1
    for i in range(2, MAX_C):
        if d[i] == -1:
            d[i] = i
            s[i] = i + 1
        else:
            j = i
            s[i] = 1

            while j % d[i] == 0:
                j //= d[i]
                s[i] = s[i] * d[i] + 1

            # d(a*b) = d(a) * d(b)
            s[i] = s[i] * s[j]

    # ex, ans[7] = 4
    for i in range(MAX_C-1, 0, -1):
        if s[i] < MAX_C:
            ans[s[i]] = i

    for _ in range(t):
        c = int(input())
        print(ans[c])


main()
