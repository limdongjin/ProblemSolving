
S = []
ans = []
def conv(ch):
    if ch == '+':
        return 1
    elif ch == '0':
        return 0
    else:
        return -1

def main():
    global S
    global ans
    n = int(input())
    S = [[0]*n for _ in range(n)]
    ans = [0]*n

    inp = input().rstrip()

    cur = 0
    for y in range(n):
        for x in range(y, n):
            S[y][x] = conv(inp[cur])
            cur += 1
    go(0)
    print(' '.join(map(str, ans)))
def is_possible(idx):
    a = 0
    for i in range(idx, -1, -1):
        a += ans[i]
        if S[i][idx] == 0 and a != 0:
            return False
        elif S[i][idx] > 0 >= a:
            return False
        elif S[i][idx] < 0 <= a:
            return False
    return True
def go(idx):
    global ans
    if idx == len(S):
        return True
    if S[idx][idx] == 0:
        ans[idx] = 0
        return is_possible(idx) and go(idx+1)

    for num in range(1, 11):
        ans[idx] = S[idx][idx]*num
        if is_possible(idx) and go(idx+1):
            return True
    return False
main()