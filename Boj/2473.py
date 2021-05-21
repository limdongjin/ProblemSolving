from sys import stdin
input = stdin.readline

def solve(a):    
    min_v = abs(sum(a[0:3]))
    min_ijk = (a[0], a[1], a[2])
    print_ret = lambda ijk: print(' '.join(map(str, ijk)))
    
    exit_flag = False
    for i in range(len(a)):
        l, r = i+1, len(a)-1
        while l < r:
            v = a[i] + a[l] + a[r]
            if abs(v) < min_v:
                min_v = abs(v)
                min_ijk = (a[i], a[l], a[r])
            if v == 0:
                print_ret(min_ijk)
                return
                
            if v < 0:
                l += 1
            else:
                r -= 1
    print_ret(min_ijk)

_ = input()
A = sorted([int(_) for _ in input().split()])

solve(A)
