from copy import deepcopy

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for y in range(N)]
Q = [tuple(map(int, input().split())) for _ in range(K)]

dy, dx = [1, 0, -1,0], [0,-1,0,1]
# D L U R

ans = 10000

def value(arr):
    return min(sum(row) for row in arr)

def convert(arr, qry):
    r, c, s = qry
    r, c = r-1, c-1
    # (r, c) : 중심점

    narr = deepcopy(arr)
    for i in range(1, s+1):
        rr, cc = r-i, c+i 
        for w in range(4):
            for d in range(i*2):
                rrr, ccc = rr+dy[w], cc+dx[w]
                narr[rrr][ccc] = arr[rr][cc]
                rr, cc = rrr, ccc
    return narr

def dfs(arr, qry):
    if sum(qry) == K:
        global ans
        ans = min(ans, value(arr))
        return
    
    for i in range(K):
        if qry[i]: continue
        narr = convert(arr, Q[i])
        
        qry[i] = 1
        dfs(narr, qry)
        qry[i] = 0
    
dfs(A, [0 for i in range(K)])

print(ans)
