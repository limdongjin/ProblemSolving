#
# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3
# 문제 제목: 소수 찾기
#


def solution(numbers):
    answer = 0
    p_numbers = possible_numbers(numbers)
    for num in p_numbers:
        answer += is_prime_number(num)
    return answer


def is_prime_number(number):
    if number < 2:
        return 0

    for i in range(2, int(number/2 + 1)):
        if number % i == 0:
            return 0
    return 1


def possible_numbers(numbers):
    result = []
    for i in range(1, len(numbers) + 1):
        for tup in permutations(numbers, r=i):
            number = ""
            for c in tup:
                number += c
            result.append(int(number))
    return list(set(result))


def product(*args, repeat=1):
    # itertools.product 내부 코드에서 yield 대신 한번에 return 하도록 수정
    # ex, product(range(2), repeat=2)
    pools = [tuple(pool) for pool in args] * repeat
    # ex, pools = [(0, 1), (0, 1)]
    result = [[]]
    for pool in pools:
        # ex, pool is (0, 1)
        result = [x + [y] for x in result for y in pool]
        # ex, first loop: result is [[0], [1]]
        # ex, second loop: result is [[0, 0], [0, 1], [1, 0], [1, 1]]
    result = [tuple(prod) for prod in result]
    # ex, result is [(0, 0), (0, 1), (1, 0), (1, 1)]
    return result


def permutations(iterable, r=None):
    # itertools.permutation 내부 코드에서 yield 대신 한번에 return 하도록 수정
    # ex, permutations("ab")
    pool = tuple(iterable)
    # ex, pool = ('a', 'b')
    n = len(pool)
    # ex, n = 2
    r = n if r is None else r
    # ex, r = 2
    result = []
    for indices in product(range(n), repeat=r):
        # ex, product(range(2), repeat=2) == [(0, 0), (0, 1), (1, 0), (1, 1)]
        # indices 는 (숫자, 숫자, ...) 형태
        if len(set(indices)) == r:
            # indices 의 숫자값들은 결국 인덱스의 조합으로 생각할수있다.
            # set()을 통해서 (0, 0) (1, 1) 과 같이 동일한 인덱스를 두번 선택하는 경우를 제외할수있다.
            result.append(tuple(pool[i] for i in indices))
            # ex, first loop: len(set((0, 0))) 은 1 이므로 조건에 해당되지않는다
            # ex, second loop: [('a', 'b')]
            # ex, third loop: [('a', 'b'), ('b', 'a')]
            # ex, last loop: len(set((1, 1))) 은 1 이므로 조건에 해당되지않는다
    # ex, [('a', 'b'), ('b', 'a')]
    return result


def test_solution():
    assert solution("17") == 3
    assert solution("011") == 2


def test_possible_numbers():
    assert possible_numbers("17").count(1) == 1
    assert possible_numbers("17").count(71) == 1
    assert possible_numbers("17").count(17) == 1
    assert possible_numbers("17").count(7) == 1

    assert possible_numbers("011").count(1) == 1
    assert possible_numbers("011").count(10) == 1
    assert possible_numbers("011").count(101) == 1
    assert possible_numbers("011").count(0) == 1
    assert len(possible_numbers("011")) == 6


def test_permutations():
    assert permutations("aaa", r=1) == [('a',), ('a',), ('a',)]
    assert permutations("aaa", r=2) == [('a', 'a'), ('a', 'a'), ('a', 'a'), ('a', 'a'), ('a', 'a'), ('a', 'a')]
    assert permutations("12", r=2) == [('1', '2'), ('2', '1')]
    assert permutations("123", r=2) == [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
    assert len(permutations("1123", r=2)) == 12
    assert len(permutations("0110231", r=3)) == 210


test_permutations()
test_possible_numbers()
test_solution()