from functools import reduce

def main():
    inp = input()

    arr = inp.split('-')
    # 마이너스를 기준으로 분리된 식은 + 또는 숫자로 이루어진 식이다.

    nums = []
    for expr in arr:
        # 플러스로만 이루어졌으니 + 로 분리해서 합하면 해당 식의 값을 알수있다.
        nums.append(sum([int(_) for _ in expr.split('+')]))

    ret = reduce(lambda a, b: a - b, nums)
    print(ret)


main()