

def main():
    tc = int(input())
    for _ in range(tc):
        m, n, x, y = [int(_) for _ in input().split()]

        cnt = x
        flag = False
        for i in range(0, n):
            ny = (x + i*m)%n
            if ny == 0:
                ny = n
            if ny == y:
                print(cnt)
                flag = True
                break
            cnt += m
        if not flag:
            print(-1)
main()