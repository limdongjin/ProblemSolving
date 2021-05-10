
class SquareMatrix:
    def __init__(self, n, data):
        self.n = n
        # 2 dimension array
        self.data = data

    @classmethod
    def identity(cls, n):
        # return identity matrix (n*n)
        data = [[0]*n for y in range(n)]
        for i in range(n):
            data[i][i] = 1
        return SquareMatrix(n, data)

    @classmethod
    def mul(cls, A, B):
        # return A*B
        n = A.n
        c = [[0]*n for i in range(n)]

        for i in range(n):
            for j in range(n):
                c[i][j] = sum([A.data[i][k]*B.data[k][j] for k in range(n)])
        return SquareMatrix(n, c)
    @classmethod
    def pow(cls, A, m):
        # return A^m
        n = A.n
        if m == 0:
            return cls.identity(n)
        if m % 2 != 0:
            return cls.mul(A, cls.pow(A, m-1))
        half = cls.pow(A, m//2)
        return cls.mul(half, half)
    @classmethod
    def print_matrix(cls, A):
        for y in range(A.n):
            for x in range(A.n):
                print(A.data[y][x], end=' ')
            print()
        print()
def main():
    n = 3
    m = 5

    data = [[1, 2, 3], [4, 5, 6], [7,8,9]]
    matrix33 = SquareMatrix(n, data)
    print('n =', n, ', m =', m)
    SquareMatrix.print_matrix(matrix33)
    ret = SquareMatrix.pow(matrix33, m)
    SquareMatrix.print_matrix(ret)

main()
