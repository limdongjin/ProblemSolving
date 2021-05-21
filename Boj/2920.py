

A = list(map(int, input().split()))
ans = '' 
flag = 0 if A[0] < A[1] else 1 # asc, desc, mixed
for i in range(2, len(A)):
    if flag == 0 and A[i-1] > A[i]:
        flag = 2
        break
    elif flag == 1 and A[i-1] < A[i]:
        flag = 2
        break

d = {0: 'ascending', 1: 'descending', 2: 'mixed'}
print(d[flag])
