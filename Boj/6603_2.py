import itertools
import sys
input =sys.stdin.readline

def solve(S):
    lottos = itertools.combinations(S, 6)
    for lotto in lottos:
        print(' '.join(map(str, lotto)))
    print()

while True:
    input1 = list(map(int, input().split()))
    N = input1[0]
    if N == 0:
        # end of program
        break
    S = input1[1:][:]
    
    solve(S)
