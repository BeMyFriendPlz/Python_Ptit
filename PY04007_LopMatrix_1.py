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
    t = int(input())
    for i in range(t):
        n, m = [int(x) for x in input().split()]
        lst = [[0] * m] * n
        for i in range (n):
            lst[i] = [int(x) for x in input().split()]
        matrix1 = Matrix(lst, n, m)
        chuyenVi = [list(x) for x in zip(*lst)]
        matrix2 = Matrix(chuyenVi, m, n)
        ans = matrix1.nhan(matrix2)
        for x in ans:
            for y in x:
                print(y, end=" ")
            print()