

def main():
    prime = []
    is_prime = [True for _ in range(1000011)]
    is_prime[0] = is_prime[1] = False
    for i in range(2, len(is_prime)):
        if is_prime[i]:
            prime.append(i)
            j = i*i
            while j < len(is_prime):
                is_prime[j] = False
                j += i
    while True:
        n = int(input())
        if n == 0:
            return
        for i in range(0, len(prime)):
            if is_prime[n - prime[i]]:
                print(n,'=',+prime[i],'+',n-prime[i])
                break

main()