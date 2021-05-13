import sys
input = sys.stdin.readline

arr = sorted(list(map(int, input().split())))
ret = 0
if len(set(arr)) == 1:
    ret = 10000 + arr[0]*1000
elif len(set(arr)) == 2:
    ret = 1000 + arr[1]*100
else:
    ret = arr[2]*100

print(ret)
