import sys
sys.setrecursionlimit(200000000)
cnt = 0
def main():
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        board = [0 for _ in range(n+1)]
        s = input().split()
        for i in range(n):
            board[i+1] = int(s[i])
        global cnt
        cnt = 0
        solve(board)
        print(n - cnt)


def solve(board):
    complete = [False for i in range(len(board) + 1)]
    visited = [False for i in range(len(board) + 1)]
    for node in range(1, len(board)):
        if not visited[node]:
            dfs(board, visited, complete, node)


def dfs(board, visited, complete, pos):
    global cnt
    visited[pos] = True
    next_node = board[pos]

    if not visited[next_node]:
        dfs(board, visited, complete, next_node)
    else:
        if not complete[next_node]:
            cur = next_node
            while cur != pos:
                cnt += 1
                cur = board[cur]
            cnt += 1
    complete[pos] = True


main()