n = int(input())

cache = [0, 1]

for i in range(2, n+1):
    ret = 1e9
    j = 1
    while j**2 <= i:
        ret = min(ret, cache[i - (j**2)])
        j += 1
    cache.append(ret + 1)

print(cache[n])