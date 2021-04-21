

def main():
    n = int(input())
    ret = 0
    for _ in range(n):
        a, b, c = [int(_) for _ in input().split()]
        if a+b+c >= 2:
            ret += 1
    print(ret)


main()