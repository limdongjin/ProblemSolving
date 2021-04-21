import sys
input = sys.stdin.readline


def main():
    n, k = [int(_) for _ in input().split()]
    k = k - 1
    scores = [int(_) for _ in input().split()]

    target = scores[k]
    ret = sum([1 for score in scores if score != 0 and target <= score])

    print(ret)


main()