from collections import deque


dirs = [(-1, 0),(0,1), (1, 0), (0, -1)]
# up rig dow lef

cw = [1, 2, 3, 0]
ccw = [1, 0, 3, 2]

def solve(t):
    for sec in range(1, t+1):
        spreadAll()
        circulate(A, airc[0], ccw)
        circulate(A, airc[1], cw)

    ret = 0
    for r in range(R):
        ret += sum(A[r])
    ret += 2 # airc

    return ret

def circulate(A, pos, cw_or_ccw):
    r, c = pos[0],pos[1] + 1
    A_clone = [A[r][:] for r in range(len(A))]
    A[r][c] = 0
    for d in cw_or_ccw:
        dr, dc = dirs[d][0], dirs[d][1]
        while True:
            nr, nc = r+dr, c+dc
            if nr < 0 or nc < 0 or nr >= R or nc >= C:
                break
            if nr == pos[0] and nc == pos[1]:
                break
            A[nr][nc] = A_clone[r][c]
            r, c = nr, nc
    return

def spreadAll():
    q = deque()
    for r in range(R):
        for c in range(C):
            if A[r][c] > 4:
                q.append((r, c, A[r][c]))
    while q:
        r, c, v = q.popleft()
        t = v // 5
        cnt = 0
        for dy, dx in dirs:
            ny, nx = r+dy, c+dx
            if ny < 0 or nx < 0 or ny >= R or nx >= C:
                continue
            if A[ny][nx] == -1:
                continue
            cnt += 1
            A[ny][nx] += t
        A[r][c] -= t*cnt


R, C, T = map(int, input().split())
airc = [] # [(ur, uc), (dr, dc)]
A = [[0]*C for r in range(R)]
for r in range(R):
    s = list(map(int, input().split()))
    for c in range(C):
        A[r][c] = s[c]
        if A[r][c] == -1:
            airc.append((r, c))

print(solve(T))
