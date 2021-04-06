import sys
input = sys.stdin.readline

n = int(input())
meetings = []
for _ in range(n):
    s, e = [int(x) for x in input().split()]
    meetings.append((s, e))

meetings.sort(key=lambda meeting: (meeting[1], meeting[0]))
end = -1
ret =0
for meeting in meetings:
    if end <= meeting[0]:
        end = meeting[1]
        ret = ret + 1
print(ret)