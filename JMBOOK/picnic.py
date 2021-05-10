

def solve(n, m, are_fr):
    checked = [False]*n
    def count_pairs(checked):
        student1 = -1
        for i in range(n):
            if not checked[i]:
                student1 = i
                break
        if student1 == -1:
            return 1
        
        ret = 0
        for p in range(student1+1, n):
            if (student1, p) in are_fr and not checked[p]:
                checked[p] = checked[student1] = True
                ret += count_pairs(checked)
                checked[p] = checked[student1] = False
        return ret

    return count_pairs(checked)

TC = int(input())
for _ in range(TC):
    n, m = map(int, input().split())
    are_fr = {}
    
    tmp = [int(i) for i in input().split()]
    for i in range(0, m*2, 2):
        a, b = tmp[i], tmp[i+1]
        are_fr[(a, b)] = True
        are_fr[(b, a)] = True

    print(solve(n, m, are_fr))

