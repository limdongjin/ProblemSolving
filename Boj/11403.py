

def main():
    n = int(input())
    board = [[0]*n for _ in range(n)]
    for i in range(n):
        s = input().split()
        for j in range(n):
            board[i][j] = int(s[j])
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        visited = [0 for _ in range(n)]
        dfs(board, visited, i)
        for k in range(n):
            if visited[k]:
                ret[i][k] = 1
    for i in range(n):
        for j in range(n):
            print(ret[i][j], end=' ')
        print()


def dfs(board, visited, n):
    for i in range(len(board)):
        if board[n][i] and not visited[i]:
            visited[i] = True
            dfs(board, visited, i)


main()