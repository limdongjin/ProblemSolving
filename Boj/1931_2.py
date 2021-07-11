

N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
A.sort(key=lambda _: (_[1], _[0]))

ret, prev_end = 0, 0
for meet in A:
    if prev_end <= meet[0]:
        ret, prev_end = ret+1, meet[1]

print(ret)