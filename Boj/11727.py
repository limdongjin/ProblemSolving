import sys

def main():
    n = int(sys.stdin.readline())
    cache = [0 for i in range(n + 10)]
    cache[1] = 1
    cache[2] = 3

    for i in range(3, n + 1):
        cache[i] = (2*cache[i -2] + cache[i - 1]) % 10007
    print(cache[n])

main()