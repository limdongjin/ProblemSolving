#  (실패한 풀이)
# 0. 예외 처리 : (M == 1) or (M == 2 and N%10 == 0) 일때, -1 출력
# 1. 가장 큰 수를 맨앞으로 옮겨준다.(큰 수가 두개 이상 존재할경우 가장 오른쪽의 큰 수와 교환함). 다음 위치에서도 이 과정을 반복
# - ex, 1788 -> 8781 (good)
# -     1788 -> 8718 (bad)
# 2. (1) 과정을 마쳤으나, 해야할 연산횟수가 이미 남았다면?
# 3. case1. 중복되는 수가 존재한다 => 연산을 더 하지않아도 된다는것
# 4. else. 일의 자리와 십의 자리끼리 연산 수행
# (실패하는 이유) 연산 중간값은 작더라도, 최종값만 크면 되기때문임..

import sys
input = sys.stdin.readline


def argmax_r(items):
    return max(range(len(items) - 1, -1, -1),
               key=lambda i: items[i])


def solve(n: str, k: int) -> str:
    # case M == 1 or M == 2
    if len(n) == 1:
        return '-1'
    if len(n) == 2:
        if n[-1] == '0':
            return '-1'
        return n[::-1] if k % 2 else n

    ret = []
    cur = list(n)

    while len(cur) != 1 and k != 0:
        i = argmax_r(cur)
        if i != 0:  # 맨앞에 숫자는 가장 커야한다.
            ret.append(cur[i])
            cur[0], cur[i] = cur[i], cur[0]
            cur = cur[1:]
            k -= 1
        elif i == 0:  # 이미 맨앞의 숫자가 가장 큰 수인 경우
            ret.append(cur[i])
            cur = cur[1:]
    ret += cur

    if k == 0:  # case1. 연산을 다 마침
        return ''.join(map(str, ret))

    assert len(cur) == 1
    assert ret == sorted(ret, reverse=True)

    # case2. ret 에 서로 같은 수가 하나 이상 존재한다면, ret 을 그대로 반환해도 된다.
    is_exist = {str(x): False for x in range(10)}
    for x in ret:
        if is_exist[x]:
            return ''.join(map(str, ret))
        is_exist[x] = True

    # else case. 가장 끝에 있는 수 끼리 교환
    k %= 2
    ret[-1], ret[-2] = ret[-2], ret[-1]
    return ''.join(map(str, ret))

def test():
    inp_exp = [
        [('12', 1), '21'],
        [('12', 2), '12'],
        [('16375', 1), '76315'],
        [('132', 3), '312'],
        [('432', 1), '423'],
        [('90', 4), '-1'],
        [('900', 2), '900'],
        [('5', 2), '-1'],
        [('436659', 2), '966354'],
        [('54432', 2), '54432'],
        [('421888', 3), '888421'], # 반례
        [('124888', 3), '888421'],
        [('214888', 3), '888421'], # 반례
        [('52676', 2), '76652'],
        [('1488', 2), '8841'],
        [('40069', 3), '96400'],
        [('10042', 2), '42010'],
        [('740792', 2), '970742'],
        [('199', 1), '991'],
        [('31299', 2), '99231'],  # 반례1
        [('4188', 2), '8841'],    # 반례2
        [('2133', 2), '3321'],    # 반례3
        [('8799', 2), '9987'],    # 반례4
    ]
    flag = True
    for inp, expected in inp_exp:
        actual = solve(*inp)
        if actual != expected:
            print('[FAIL] inp=', inp, ':', actual, '!=', expected, ': (actual != expected)')
            flag = False
    if not flag:
        assert False  # test fail

if __name__ == '__main__':
    test()
    N, K = input().split()
    K = int(K)

    print(solve(N, K))

# 반례1
# assert solve('31299', 2) == '99231'
# 31299 -> 91293 -> 99213 (X)
# 31299 -> 91239 -> 99231 (0)

# assert solve('1488', 2) == '8841'
# 반례2
# assert solve('4188', 2) == '8841'
# 4188 -> 8184 -> 8814 (X)
# 4188 -> 8148 -> 8841 (0)

# 반례3
# assert solve('2133', 2) == '3321'
# 2133 -> 3132 -> 3312 (X)
# 2133 -> 3123 -> 3321 (0)

# 반례4
# assert solve('8799', 2) == '9987'
# 8799 -> 9 798 -> 99 78 (X)
# 8799 -> 9 789 -> 99 87 (0)

# 1799 -> 9791 -> 9971 (0)
# 1799 -> 9719 -> 9917 (X)