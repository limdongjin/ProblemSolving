import sys
input = sys.stdin.readline

def main():
    tc = int(input())

    for _ in range(tc):
        n = int(input())
        d = dict()

        for i in range(n):
            _, key = input().split()
            d[key] = d.get(key, 0) + 1

        ret = 1
        for val in d.values():
            ret *= (val+1)
        ret -= 1
        print(ret)
main()