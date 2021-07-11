import sys
input = sys.stdin.readline

def solve(a, b, c):
    def _recursive_mul(aa, bb, cc):
        if bb == 0 or bb == 1:
            return aa ** bb
        
        if bb%2 == 0:
            ret = _recursive_mul(aa, bb//2, cc)
            return pow(ret, 2)%cc
        else:
            return (_recursive_mul(aa, bb-1, cc)*aa)

    return _recursive_mul(a%c, b, c)%c
A, B, C = map(int, input().split())
print(solve(A, B, C))
