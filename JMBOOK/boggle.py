
def read_input():
    f = open('boggle_input.txt', 'r')
    
    n, m, word = f.readline().split()
    n = int(n)
    m = int(m)
    board = [ ['.']*m for y in range(n)]
    for y in range(n):
        line = f.readline()
        for x in range(m):
            board[y][x] = line[x]

    return board, word

def print_board(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            print(board[y][x], end='')
        print()
    return

def has_word(board, word):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    def _has_word(yx, target):
        y, x = yx
        if board[y][x] != target[0]:
            return False
        if len(target) == 1:
            return True

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if ny < 0 or nx < 0:
                continue
            if ny >= len(board) or nx >= len(board[0]):
                continue
            if _has_word((ny, nx), target[1:]):
                return True
        return False

    for y in range(len(board)):
        for x in range(len(board[0])):
            if _has_word((y, x), word):
                return True
    return False


board, word = read_input()
print_board(board)
print('has', word, has_word(board, word))

