
def rotate90(N, board):
    nb = [[0]*N for y in range(N)]
    for y in range(N):
        for x in range(N):
            nb[x][N-y-1] = board[y][x]
    return nb

def convert(N, row):
    # execute left action
    
    tmp = list(filter(lambda v: v != 0, row))
    for i in range(1, len(tmp)):
        if tmp[i-1] == tmp[i]:
            tmp[i-1] *= 2
            tmp[i] = 0
    tmp = list(filter(lambda v: v != 0, tmp))
    return tmp + [0]*(N-len(tmp))

def dfs(N, board, cnt):
    ret = max(max(row) for row in board)

    if cnt == 0: return ret
    for _ in range(4):
        # cb : (left)converted board
        # row 마다 convert 한 row 를 저장 
        cb = [convert(N, row) for row in board]
        
        if cb != board: # convert 된값이 있다는 것 
            ret = max(ret, dfs(N, cb, cnt-1))

        board = rotate90(N, board)
    return ret

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

print(dfs(N, board, 5))
