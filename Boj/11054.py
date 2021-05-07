import sys
input = sys.stdin.readline
def main():
    n = int(input())
    A = list(map(int, input().split()))
    # D[i] : i 로 끝나는가장 긴 증가 부분 수열 길이 
    D = [1]*n

    # D2[i] : i 로 시작하는 가장 긴 감소 부분수열 길이 
    D2 = [1]*n

    for i in range(n):
        D[i] += max([0] + 
                    [ D[j] for j in range(i) 
                        if A[i] > A[j] ])

    for i in range(n-1, -1, -1):
        D2[i] += max([0] + 
                     [ D2[j] for j in range(i+1, n) 
                        if A[i] > A[j] ])
    print(max([D[i]+D2[i]-1 for i in range(n)]))

main()
