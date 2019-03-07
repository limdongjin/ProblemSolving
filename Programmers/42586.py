#
# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3
# 문제 제목: 기능 개발
#


def solution(progresses, speeds):
    answer = []

    while True:
        if len(progresses) == 0:
            break
        i = 0
        while i < len(progresses):
            progresses[i] += speeds[i]
            i += 1
        if progresses[0] >= 100:
            removed_progress = []
            i = 0
            for progress in progresses:
                if progress >= 100:
                    removed_progress.append(i)
                else:
                    break
                i += 1
            new_progresses = []
            i = 0
            for progress in progresses:
                if removed_progress.count(i) == 0:
                    new_progresses.append(progress)
                i += 1
            i = 0
            new_speeds = []
            for speed in speeds:
                if removed_progress.count(i) == 0:
                    new_speeds.append(speed)
                i += 1
            progresses = new_progresses
            speeds = new_speeds
            answer.append(len(removed_progress))
    return answer


def test_solution():
    assert solution([1, 1, 1], [1, 1, 1]) == [3]
    assert solution([99, 99, 99], [1, 1, 1]) == [3]
    assert solution([1], [1]) == [1]
    assert solution([1, 1], [1, 1]) == [2]
    assert solution([1, 1], [2, 1]) == [1, 1]
    assert solution([93, 30, 55], [1, 30, 5]) == [2, 1]
    assert solution([93, 30, 55], [1, 5, 30]) == [1, 2]
    assert solution([1, 99, 99], [1, 1, 1]) == [3]
    assert solution([20, 99, 1], [30, 1, 1]) == [2, 1]
    assert solution([20, 30, 40, 50], [10, 1, 20, 10]) == [1, 3]
    assert solution([20, 30, 40, 50], [10, 20, 5, 5]) == [2, 2]
    assert solution([20, 30, 40, 50], [10, 20, 5, 1]) == [2, 1, 1]
    assert solution([20, 30, 40, 50], [10, 20, 1, 10]) == [2, 2]


test_solution()
