import sys
input = sys.stdin.readline

def solve(a):
    # is increasing sorted
    if all(a[i-1] <= a[i] for i in range(1,len(a))):
        return 0
 
    # is decreasing sorted
    if all(a[i-1] >= a[i] for i in range(1,len(a))):
        return 0
    start = 0    
    u_flag = False
    d_flag = True
    for i in range(len(a)-1, 0, -1):
        if d_flag and not(a[i-1] >= a[i]):
            u_flag = True
            d_flag = False
        elif u_flag and not(a[i-1] <= a[i]):
            start = i
            break
    return start
 
t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(num) for num in input().split()]
    
    print(solve(nums))
