

def main():
    n = int(input())

    # n//i : i 가 나오는 횟수
    print(sum([i*(n//i) for i in range(1, n+1)]))


main()