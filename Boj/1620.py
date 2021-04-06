import sys

input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
book = {}
for i in range(1, n + 1):
    name = input().rstrip()
    book[name] = i
    book[str(i)] = name

for _ in range(m):
    ret = book.get(input().rstrip())
    print(ret)
