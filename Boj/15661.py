import sys
d = []
def main():
    global d
    n = int(input())
    d = [[0]*n for _ in range(n)]
    for y in range(n):
        s = list(map(int, input().split()))
        for x in range(n):
            d[y][x] = s[x]

    print(go(idx=0, team1=[], team2=[]))

def go(idx, team1, team2):
    n = len(d)
    if idx == n:
        if len(team1) == 0 or len(team2) == n:
            return sys.maxsize
        t1 = 0
        t2 = 0
        for p1 in range(len(team1)):
            for p2 in range(len(team1)):
                if p1 == p2:
                    continue
                t1 += d[team1[p1]][team1[p2]]

        for p1 in range(len(team2)):
            for p2 in range(len(team2)):
                if p1 == p2:
                    continue
                t2 += d[team2[p1]][team2[p2]]

        return abs(t1 - t2)

    ans = go(idx+1, team1+[idx], team2)
    t2 = go(idx+1, team1, team2+[idx])

    return min(ans, t2)

main()