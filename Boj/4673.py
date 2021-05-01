def self_num(i):
    ret = i
    n = i
    while n:
        ret += n % 10
        n //= 10
    return ret

def main():
    nums = [True]*10010

    for i in range(1, 10001):
        n  = self_num(i)
        if n > 10000:
            continue
        nums[n] = False
     
    for i in range(1, 10001):
        if nums[i]:
            print(i)


main()
