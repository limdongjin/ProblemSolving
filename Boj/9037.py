import sys
input=sys.stdin.readline
def all_same(arr):
    return len(set(arr)) == 1

def go(candy):
    old = candy[:]
    for i in range(len(candy)):
        candy[i] = old[i]//2 + old[i-1]//2
        if candy[i]%2:
            candy[i] += 1
    
    return

def solve(N, candy):
    ret = 0

    # 처음부터 홀수인 애들 보충 
    for i in range(len(candy)):
        if candy[i]%2:
            candy[i] += 1
    
    while not all_same(candy):
        ret += 1
        go(candy)
    return ret


TC = int(input())
for _ in range(TC):
    N, candy = int(input()), list(map(int, input().split()))
    print(solve(N, candy))
