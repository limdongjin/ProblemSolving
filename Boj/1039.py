import sys
from collections import deque

input = sys.stdin.readline


def swap(s: str, i: int, j: int) -> str:
    s = list(s)
    s[i], s[j] = s[j], s[i]
    return ''.join(s)


def bfs(q: deque) -> int:
    visited = set()

    # qsize : queue 에 원래 들어있던 요소 개수
    qsize = len(q)

    for _ in range(qsize):
        num = q.popleft()
        if num in visited:
            continue
        visited.add(num)
        str_num = str(num)

        # str_num으로 만들 수 있는 모든 경우를 queue 에 넣는다.
        for i in range(len(str_num) - 1):
            for j in range(i + 1, len(str_num)):
                if i == 0 and str_num[j] == '0':
                    continue
                str_num = swap(str_num, i, j)
                q.append(int(str_num))
                str_num = swap(str_num, i, j)


def greedy_solve(n: str, k: int) -> str:
    def argmax_r(items):
        return max(range(len(items) - 1, -1, -1),
                   key=lambda i: items[i])

    ret = []
    cur = list(n)

    while len(cur) != 1 and k != 0:
        i = argmax_r(cur)
        if cur[0] != cur[i]:  # 맨앞에 숫자는 가장 커야한다.
            ret.append(cur[i])
            cur[0], cur[i] = cur[i], cur[0]
            cur = cur[1:]
            k -= 1
        else:  # 이미 맨앞의 숫자가 가장 큰 수인 경우
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
    if k == 1:
        ret[-1], ret[-2] = ret[-2], ret[-1]
    return ''.join(map(str, ret))

def is_greedy_possible(n: str, k: int) -> bool:
    if k == 1:
        return True
    len_n = len(n)
    if len_n == 3:
        return True

    set_n = set(n)
    if len(set_n) == len_n:
        # 중복 되는 수가 없다면 그리디 가능
        return True
    if len(set_n) == 1:
        # 하나의 수만 존재
        return True
    d = {num: n.count(num) for num in set_n}
    dup_nums = set(filter(lambda x: d[x] > 1, d))
    sorted_n = sorted(list(set_n), reverse=True)

    if len_n == 4:  # (3, 1), (2, 2)
        if sorted_n[0] not in dup_nums:
            # 가장 큰 수가 중복이 아니면, 그리디 가능
            return True
        if len(dup_nums) == 2:
            # 중복 쌍이 두개, 그리디 가능
            return True
        if d[sorted_n[0]] == 3:
            # 가장 큰 수가 3개 중복, 그리디 가능
            # ex, 2999
            return True
    elif len_n == 5:  # (4,1) (3 2) (3 1 1) (2 2 1) (2 1 1 1)
        if sorted_n[0] not in dup_nums and \
                sorted_n[1] not in dup_nums:
            return True
        # 42554 -> 52454 -> 55424 (not greedy)
        # 45255 -> 55245 -> 55542 (not greedy)
        if len(dup_nums) == 2 and \
                sum(d[num] for num in dup_nums) == 5:
            # (4,1) (3,2)
            return True

        if d[sorted_n[0]] == 4 or \
                d[sorted_n[1]] >= 3:
            return True
    elif len_n == 6:  # (5,1) (4,2) (4,1,1) (3 3) (3 2 1) (3 1 1 1) (2 2 2) ( 2 1 1 1 1)
        if len(dup_nums) == 2 and \
                sum(d[num] for num in dup_nums) == 6:
            return True

        if sorted_n[0] not in dup_nums and \
                sorted_n[1] not in dup_nums and \
                sorted_n[2] not in dup_nums:
            return True

        if d[sorted_n[0]] >= 5 or \
                d[sorted_n[1]] >= 4 or \
                d[sorted_n[2]] >= 3:
            return True
    return False

def solve(n: str, k: int) -> str:
    # case M == 1 or M == 2
    if len(n) == 1:
        return '-1'
    if len(n) == 2:
        if n[-1] == '0':
            return '-1'
        return n[::-1] if k % 2 else n
    if is_greedy_possible(n, k):
        return greedy_solve(n, k)

    q = deque()
    q.append(int(n))

    for _ in range(k):
        bfs(q)

    return str(max(q))


def test():
    inp_exp = [
        [('909', 1), '990'],
        [('120', 3), '210'],
        [('178628', 1), '878621'],
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
        [('421888', 3), '888421'],  # 반례
        [('124888', 3), '888421'],
        [('214888', 3), '888421'],  # 반례
        [('52676', 2), '76652'],
        [('1488', 2), '8841'],
        [('40069', 3), '96400'],
        [('10042', 2), '42010'],
        [('740792', 2), '970742'],
        [('199', 1), '991'],
        [('31299', 2), '99231'],  # 반례1
        [('4188', 2), '8841'],  # 반례2
        [('2133', 2), '3321'],  # 반례3
        [('8799', 2), '9987'],  # 반례4
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
    # test()

    N, K = input().split()
    K = int(K)
    print(solve(N, K))
