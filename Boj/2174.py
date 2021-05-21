import sys
input=sys.stdin.readline

A, B = map(int, input().split())
N, M = map(int, input().split())

# 1: wall, 0: blank, etc: robot 
board = [['0']*(A+2) for _ in range(B+2)]
dirs = {'N': (1,0),'E': (0,1),'S': (-1,0),'W': (0,-1)}

# 벽 세우기 
for x in range(A+2):
    board[0][x] = '1'
    board[B+1][x] = '1'
for y in range(B+2):
    board[y][0] = '1'
    board[y][A+1] = '1'

# 로봇 세우기 
robots = [[0]]
for _ in range(N):
    c, r, d = input().split()
    c, r = int(c), int(r)
    robots.append([r, c, d])
    board[r][c] = d

is_wall = lambda r, c: board[r][c] == '1'
is_crash = lambda r, c: board[r][c] != '0'

coms = [input().split() for _ in range(M)]
for comm in coms:
    rid, com, cnt = comm
    rid, cnt = int(rid), int(cnt)
    robot = robots[rid]
    r, c, d = robot

    if com in 'LR':
        cnt = cnt%4
        cnt = cnt if com == 'L' else -cnt
        robot[2] = 'NWSE'[('NWSE'.index(d)+cnt)%4]
        board[r][c] = robot[2]
        continue
    
    for _ in range(cnt):
        r, c, d = robot
        nr, nc = r+dirs[d][0], c+dirs[d][1]
        if is_wall(nr, nc):
            # crash wall
            print('Robot {} crashes into the wall'.format(rid))
            sys.exit()
        
        if is_crash(nr, nc):
            # crash robot

            # find (nr, nc) robot
            nrid = -1
            for rrid in range(1, len(robots)):
                if robots[rrid][0]==nr and robots[rrid][1]==nc:
                    nrid = rrid
                    break

            print('Robot {} crashes into robot {}'.format(rid, nrid))
            sys.exit()
        
        # move (r,c) to (nr, nc)
        board[r][c] = '0'
        robot[0], robot[1] = nr, nc
        board[nr][nc] = d

print('OK')
