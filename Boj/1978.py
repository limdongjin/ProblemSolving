

def main():
    n = int(input())
    nums = [int(_) for _ in input().split()]

    is_prime = [True for _ in range(1001)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, 1001):
        if is_prime[i]:
            j = i*i
            while j <= 1000:
                is_prime[j] = False
                j += i
    print(sum([is_prime[num] for num in nums]))

main()