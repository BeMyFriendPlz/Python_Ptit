import sys

class Matrix:
    def __init__(self, matrix, n, m) -> None:
        self.matrix = matrix
        self.n = n
        self.m = m
    
    def nhan(self, other):
        ans = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.m):
                    ans[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return ans

if __name__ == "__main__":
    a = []
    for line in sys.stdin: a += map(int, line.split())
    idx = 1
    for i in range(a[0]):
        n, m = a[idx], a[idx + 1]
        idx += 2
        lst = [[0 for x in range(m)] for x in range(n)]
        for i in range (n):
            for j in range(m):
                lst[i][j] = a[idx]
                idx += 1
        matrix1 = Matrix(lst, n, m)
        chuyenVi = [list(x) for x in zip(*lst)]
        matrix2 = Matrix(chuyenVi, m, n)
        ans = matrix1.nhan(matrix2)
        for x in ans:
            for y in x:
                print(y, end=" ")
            print()