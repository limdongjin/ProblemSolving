
def test_solution():
    board = [[0 ,0 ,0 ,0 ,0] ,[0 ,0 ,1 ,0 ,3] ,[0 ,2 ,5 ,0 ,1] ,[4 ,2 ,4 ,4 ,2] ,[3 ,5 ,1 ,3 ,1]]
    moves = [1 ,5 ,3 ,5 ,1 ,2 ,1 ,4]
    expected = 4

    assert solution(board, moves) == expected

def solution(board, moves):
    W, H, ret = len(board[0]), len(board), 0
    stack = []
    moves = [move-1 for move in moves]

    # 가장 위에 있는 인형 위치를 저장한다.
    # board[-1][col] : col 컬럼에서 가장 위에 있는 인형의 라인 번호
    board.append([])
    for x in range(W):
        y = 0
        while y < H and board[y][x] == 0:
            y += 1
        board[-1].append(y)

    for move in moves:
        top = board[-1][move]

        # move 컬럼에 인형이 없는 경우
        if top >= H:
            continue

        stack.append(board[top][move])
        board[top][move] = 0
        board[-1][move] = top+1

        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            ret += 2
    print(ret)
    return ret


test_solution()