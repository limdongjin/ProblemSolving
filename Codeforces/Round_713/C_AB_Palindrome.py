

def main():
    tc = int(input())
    for _ in range(tc):
        a, b = [int(_) for _ in input().split()]
        s = [ch for ch in input().rstrip()]
        flag = False
        for i, ch in enumerate(s):
            if ch != '?':
                if s[~i] == '?':
                    s[~i] = ch
                elif ch != s[~i]:
                    print('-1')
                    flag = True
                    break
        if flag:
            continue
        a -= s.count('0')
        b -= s.count('1')
        ab = s.count('?')
        if a + b != ab or a < 0 or b < 0 or (a%2 == 1 and b%2 == 1):
            print('-1')
            continue
        if a%2 == 1 or b%2 == 1:
            # odd
            mid = len(s) // 2
            if s[mid] != '?':
                print('-1')
                continue
            if a%2 == 1:
                s[mid] = '0'
                a -= 1
            else:
                s[mid] = '1'
                b -= 1
        for i in range(len(s)):
            if s[i] == '?':
                if a > 0:
                    s[i] = '0'
                    s[~i] = '0'
                    a -= 2
                elif b > 0:
                    s[i] = '1'
                    s[~i] = '1'
                    b -= 2
        print(''.join(s))
main()