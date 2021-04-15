import sys
input = sys.stdin.readline

def main():
    n = int(input())
    m = int(input())
    s = input()
    patt = 0
    ret = 0

    i = 1
    while i < m - 1:
        if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == 'I':
            patt += 1
            if patt == n:
                ret += 1
                patt -= 1
            i += 2
        else:
            patt = 0
            i += 1

    print(ret)
main()