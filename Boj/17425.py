import sys
input = sys.stdin.readline

def main():
    t = int(input())

    # d[i] 는 f(i) 를 의미. 즉 i 의 약수의 합
    d = [1 for _ in range(1000001)]

    for i in range(2, len(d)):
        j = 1
        while i*j < len(d):
            d[i*j] += i
            j += 1

    # s[i] 는 g(i) 를 의미.
    s = [0 for _ in range(len(d))]
    for i in range(1, len(d)):
        s[i] = s[i-1] + d[i]

    ret = []
    for _ in range(t):
        n = int(input())
        ret.append(str(s[n]))

    print('\n'.join(ret))

main()