


def main():
    start = int(input())
    end = int(input())
    is_prime = [True]*(end + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, end + 1):
        if is_prime[i]:
            for j in range(i*i, end+1, i):
                is_prime[j] = False

    prime = [ i for i in range(start, end+1) if is_prime[i]]
    if not prime:
        print(-1)
    else:
        print(sum(prime))
        print(prime[0])

main()
