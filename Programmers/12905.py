#
# https://programmers.co.kr/learn/courses/30/lessons/12905
# 가장 큰 정사각형 찾기
#


def solution(board):
    low_len = len(board)
    col_len = len(board[0])
    min_len = min(low_len, col_len)
    yi = 0
    non_zero_flag = 0
    h = {}
    # { "칼럼인덱스": { "숫자": "개수" } }
    for y in board:
        xi = 0
        flag = 0
        for x in y:
            if x == 0:
                flag = 0
                xi += 1
                continue
            non_zero_flag = 1
            flag += 1
            board[yi][xi] = flag
            if h.get(xi) is None:
                h[xi] = {}
            xi += 1
        yi += 1
    if non_zero_flag == 0:
        return 0
    for xi in range(0, col_len):
        for yi in range(0, low_len):
            target = board[yi][xi]
            if target != 0 and h[xi].get(target) is None:
                h[xi][target] = 0
                cnt = 0
                max_cnt = 0
                for yyi in range(0, low_len):
                    if board[yyi][xi] < target:
                        cnt = 0
                        continue
                    cnt += 1
                    if cnt > max_cnt:
                        max_cnt = cnt
                h[xi][target] = max_cnt
    keys = list(h.keys())
    keys.sort(reverse=True)
    max_i = 1
    for i in range(2, min_len + 1):
        for key in keys:
            if key + 1 < i:
                break
            cnt = 0
            sorted_h_key_keys = sorted(h[key].keys(), reverse=True)
            for k in sorted_h_key_keys:
                if k < i:
                    cnt = 0
                    break
                if h[key][k] >= i:
                    cnt = h[key][k]
                    break
            if cnt >= i:
                max_i = i
                break
    return max_i*max_i


def test_solution():
    assert solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]) == 9
    assert solution([[0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1,1,1], [0, 0, 1, 1,1,1]]) == 16
    assert solution([[0, 0, 1, 1], [1, 1, 1, 1]]) == 4
    assert solution([[1], [1]]) == 1
    assert solution([[1, 1], [1, 1]]) == 4
    assert solution([[0, 0], [0, 0]]) == 0
    assert solution([[1, 1, 0], [1,0,0]]) == 1
    assert solution([[1, 1, 0], [1,1,0]]) == 4
    assert solution([[0],[0]]) == 0
    assert solution([[1, 1, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1]]) == 4


test_solution()
