import sys
input = sys.stdin.readline

def main():
    n = int(input())
    cnt = 0
    for _ in range(n):
        s = input().rstrip()
        cnt += 1 if go(s) else 0

    print(cnt)

def go(s):
    dic = {}
    prev = None
    for c in s:
        if c in dic:
            if prev == c:
                continue
            else:
                return False
        else:
            prev = c
            dic[c] = True
    return True
main()
