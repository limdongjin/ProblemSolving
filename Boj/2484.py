import sys
input=sys.stdin.readline
def money():
    arr = sorted(list(map(int, input().split())))
    t = len(set(arr))
    if t == 1:
        # 4same
        return arr[0]*5000 + 50000
    if t == 2:
        if arr[1] == arr[2]:
            # 3same
            return 10000 + arr[1]*1000
        else:
            # 2same, 2same
            return 2000 + arr[1]*500 + arr[2]*500
    # 2same
    for i in range(3):
        if arr[i] == arr[i+1]:
            return 1000 + arr[i]*100
    
    # not same
    return arr[-1]*100
N = int(input())
print(max(money() for i in range(N)))
