from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 超出时间限制
        count = 0
        for i in range(row1, row2):
            for j in range(col1, col2):
                count += self.matrix[i][j]
        return count

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sumr = 0
        for i in range(row1, row2 + 1):
            sumr += sum(self.matrix[i][col1:col2 + 1])
        return sumr
