import sys

def main():
    n = int(input())
    d = [[0]*n for _ in range(n)]
    for y in range(n):
        s = list(map(int, input().split()))
        for x in range(n):
            d[y][x] = s[x]

    print(go(idx=0, team1=[], team2=[], d=d))


def go(idx, team1, team2, d):
    n = len(d)
    half_n = n//2
    if idx == n:
        # impossible case
        if len(team1) != half_n or len(team2) != half_n:
            return sys.maxsize

        # calculate team ability
        t1 = 0
        t2 = 0
        for p1 in range(half_n):
            for p2 in range(half_n):
                if p1 == p2:
                    continue
                t1 += d[team1[p1]][team1[p2]]
                t2 += d[team2[p1]][team2[p2]]

        # diff of team1,team2
        return abs(t1 - t2)

    # impossible case
    # backtracking
    if len(team1) > half_n:
        return sys.maxsize
    elif len(team2) > half_n:
        return sys.maxsize

    # select team1 case
    t1 = go(idx + 1, team1 + [idx], team2, d)

    # select team2 case
    t2 = go(idx + 1, team1, team2 + [idx], d)

    ans = min(t1, t2)
    return ans


main()