import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

def main():
    N = int(input())
    
    # board[N+1][N+1] 
    board = [[-1 for idx in range(N+1)] for level in range(N+1)]
    cache = [[-1 for idx in range(N+1)] for level in range(N+1)]
    
    for level in range(1, N+1):
        s = list(map(int, input().split()))
        for idx in range(1, len(s)+1):
            board[level][idx]= s[idx-1]
            if level == N:
                cache[level][idx] = board[level][idx]
        
    print(go(1, 1, board, cache))

def go(level, idx, board, cache):
    if cache[level][idx] != -1:
        return cache[level][idx]

    cache[level][idx] = max(go(level+1, idx, board, cache), go(level+1, idx+1, board, cache)) + board[level][idx]
    return cache[level][idx]
    
main()
            
