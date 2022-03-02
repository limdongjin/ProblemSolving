from sys import stdin
import math

input = stdin.readline


def find_primes(n):
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = is_prime[1] = False

    for x in range(int(math.sqrt(n)) + 1):
        if not is_prime[x]:
            continue
        for v in range(x + x, n + 1, x):
            is_prime[v] = False
    primes = [x for x in range(n + 1) if is_prime[x]]
    return primes


def solve(n):
    primes = find_primes(n)
    if len(primes) == 0:
        return 0
    ret, m = 0, len(primes)
    half_n = n // 2
    right = cur_sum = 0
    for left in range(m):
        if primes[left] > half_n:
            break
        while cur_sum < n and right < m:
            cur_sum += primes[right]
            right += 1
        if cur_sum == n:
            ret += 1
        cur_sum -= primes[left]

    if primes[-1] == n:
        ret += 1

    return ret


if __name__ == '__main__':
    print(solve(int(input())))
