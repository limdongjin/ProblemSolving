

def main():
    n = int(input())
    five = 0

    # 끝에 0의 개수는 10 이 몇번 곱해지느냐에 달려있다.
    # 즉 소인수로 2 와 5 를 몇개 갖고있느냐를 구하면 된다.
    # 팩토리얼의 경우에는 직관적으로 봐도 5의 개수보다는 2의 개수가 훨씬 많다.
    # 즉 5의 개수만 구해도 10이 몇번 곱해지는지 알수있다.

    i = 5
    while i <= n:
        five += n//i
        i *= 5
    print(five)

main()