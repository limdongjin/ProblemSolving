import sys

def main():
    N = int(input())

    # d[N] = sum d[N-i2] 
    d = [0]*(N+5)
    d[1] = 1
    d[2] = 2
    for i in range(3, N+1):
        j = 1
        d[i] = i
        while j*j <= i:
            d[i] = min(d[i - j*j] + 1, d[i])
            j += 1
    print(d[N])


main()
