

t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(v) for v in input().split()]
    ret =  []
    d = {}

    for num in nums:
        if num in d:
            continue
        d[num] = True
        ret.append(num)
    
    print(' '.join(map(str, ret)))
