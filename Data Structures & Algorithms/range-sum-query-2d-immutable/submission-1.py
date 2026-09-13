class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.cumSums = []
        for row in matrix:
            cumsum = [row[0]]
            for elm in row[1:]:
                cumsum.append(elm + cumsum[-1])
            self.cumSums.append(cumsum)
        
        print(self.cumSums)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for r in range(row1, row2 + 1):
            sum += self.matrix[r][col1]
            sum += self.cumSums[r][col2] - self.cumSums[r][col1]
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

