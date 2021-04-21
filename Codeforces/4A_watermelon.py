import sys

input = sys.stdin.readline


def main():
    n = int(input())

    print('NO' if n % 2 or n <= 2 else 'YES')


main()
