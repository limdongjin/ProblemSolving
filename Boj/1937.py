import sys
sys.setrecursionlimit(250000000)
n: int = int(input())
board = [[0] * n for _ in range(n)]

for y in range(n):
    s = input().split()
    for x in range(n):
        board[y][x] = int(s[x])
visited = [[0] * n for _ in range(n)]


def solve():
    ret = -1
    ret_pos = ()
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                tmp = dfs((y, x))
                if ret < tmp:
                    ret = tmp
                    ret_pos = (y, x)
    # print(ret_pos)
    print(ret)


def visiting(pos):
    visited[pos[0]][pos[1]] = True

def get_next_pos(pos, dirr):
    return pos[0] + dirr[0], pos[1] + dirr[1]

def is_out_idx(idx):
    return idx < 0 or idx >= n
def is_visit(pos):
    return visited[pos[0]][pos[1]]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cache = [[-1]*n for _ in range(n)]
def dfs(pos):
    visiting(pos)
    ret = 1
    for dirr in dirs:
        ny, nx = get_next_pos(pos, dirr)
        if is_out_idx(ny) or is_out_idx(nx):
            continue
        # if is_visit((ny, nx)):
        #     continue
        if board[ny][nx] <= board[pos[0]][pos[1]]:
            continue
        if cache[ny][nx] == -1:
            dfs((ny, nx))
        # print(ny, nx, cache[ny][nx])
        ret = max(ret, cache[ny][nx] + 1)
    cache[pos[0]][pos[1]] = ret
    return ret
solve()
