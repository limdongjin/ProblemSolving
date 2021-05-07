import sys
input = sys.stdin.readline
def main():
    NINE = 9
    heights = []
    for _ in range(NINE):
        heights.append(int(input()))

    heights.sort()
    sum_h = sum(heights)
    combinations_h = combinations(heights, 2)
    
    for a, b in combinations_h:
        if sum_h - a -b == 100:
            print('\n'.join([str(h) for h in heights
                if h != a and h != b]))
            break

def combinations(seq, r):
    ret = []
    n = len(seq)
    tmp = [0]*r
    visited = [False]*n
    def _combinations(chosen, start):
        if len(chosen) == r:
            ret.append(chosen[:])
            return
        for i in range(start, n):
            if visited[i]:
                continue
            visited[i] = True
            chosen.append(seq[i])
            _combinations(chosen, start=i+1)
            chosen.pop()
            visited[i] = False
    _combinations(chosen=[], start=0)
    return ret
main()
