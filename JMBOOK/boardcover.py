import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)
def solve(board, pos):
    y, x = pos
    if is_end(pos):
        return 1
    npos = next_pos(pos, len(board),len(board[0]))
    if board[y][x] == 1:
        return solve(board, npos)
        
    ret = 0
    for type_id in range(4):
        if cover(board, pos, type_id):
            ret += solve(board, npos)
            uncover(board, pos, type_id)
    
    return ret

def cover(board, pos, type_id):
    tmp = []
    for dy, dx in BLOCKS[type_id]:
        y, x = pos[0]+dy, pos[1]+dx
        if y < 0 or x < 0 or y >= len(board) or x >= len(board[0]):
            return False
        if board[y][x]:
            return False
        tmp.append((y, x))
    for y, x in tmp:
        board[y][x] = 1
    return True

def uncover(board, pos, type_id):
    for dy, dx in BLOCKS[type_id]:
        y, x = pos[0]+dy, pos[1]+dx
        board[y][x] = 0
    return

def is_end(pos):
    return pos[0] == -1

def next_pos(pos, h, w):
    y, x = pos
    ny, nx = divmod(y*w+x+1, w)
    return (ny, nx) if ny < h else (-1, -1)

BLOCKS = [
    [(0,0), (1, -1), (1, 0)],
    [(0,0), (1, 0), (1, 1)],
    [(0,0), (1, 0), (0, 1)],
    [(0,0), (0, 1), (1, 1) ]
]
TC = int(input())
for _ in range(TC):
    H, W = map(int, input().split())
    board = [[0]*W for y in range(H)]
    for y in range(H):
        line = input()
        for x in range(W):
            board[y][x] = 0 if line[x] == '.' else 1 
    print(solve(board, (0, 0) ))

