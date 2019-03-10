#
# https://programmers.co.kr/learn/courses/30/lessons/42841?language=python3
# 문제 제목: 숫자 야구
#


def solution(baseball):
    answer = 0
    cases = [[0]] # default cases[x][y][z] = 1.
                  # not answer number is 0
    for x in range(1, 10):
        print(x)
        cases.append([[]])
        for y in range(1, 10):
            if y == x:
                cases[x].append([[]])
                continue
            cases[x].append([[]])
            for z in range(1, 10):
                if z == y or x == z:
                    cases[x][y].append(0)
                    continue
                cases[x][y].append(1)
    for ball in baseball:
        for x in range(1, 10):
            for y in range(1, 10):
                if y == x:
                    continue
                for z in range(1, 10):
                    if z == y or x == z:
                        continue
                    if [ball[1], ball[2]] != calculate_baseball_score(ball[0], x*100+y*10+z):
                        cases[x][y][z] = 0
    for x in range(1, 10):
        for y in range(1, 10):
            if y == x:
                continue
            for z in range(1, 10):
                if z == y or x == z:
                    continue
                print(x, y, z, cases[x][y][z])
                if cases[x][y][z] == 1:
                    answer += 1
    print(answer)
    return answer


def calculate_baseball_score(left, right):
    # ex, return [1, 1] 스트라이크 개수, 볼 개수
    strike = 0
    ball = 0
    if int(left//100) == int(right//100):
        strike += 1
    elif int(left//100) == int((right//10)%10):
        ball += 1
    elif int(left//100) == int(right%10):
        ball += 1
    if int((left // 10)%10) == int((right // 10)%10):
        strike += 1
    elif int((left // 10)%10) == int(right%10):
        ball += 1
    elif int((left//10)%10) == int(right//100):
        ball += 1
    if int(left % 10) == int(right % 10):
        strike += 1
    elif int(left%10) == int(right//100):
        ball += 1
    elif int(left % 10) == int((right//10)%10):
        ball += 1
    return [strike, ball]


def test_solution():
    assert solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]) == 2


def test_calculate_baseball_score():
    assert calculate_baseball_score(123, 324) == [1, 1]


test_calculate_baseball_score()
test_solution()