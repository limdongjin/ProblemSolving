
def main():
    tc = int(input())
    cache = [0 for i in range(103)]
    cache[1] = 1
    cache[2] = 1
    cache[3] = 1
    cache[4] = 2

    for _ in range(tc):
        n = int(input())
        print(solve(cache, n))

def solve(cache, n):
    if cache[n]:
        return cache[n]

    cache[n] = solve(cache, n - 2) + solve(cache, n-3)
    return cache[n]

main()