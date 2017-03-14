class NumMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        if self.matrix:
            self.dp_matrix = self._build_dp_matrix()

    def _build_dp_matrix(self):
        dp = []
        for x in range(len(self.matrix)+1): dp.append([0] * (len(self.matrix[0])+1))
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                dp[row][col] = self.matrix[row-1][col-1] + dp[row-1][col] + dp[row][col-1] - dp[row-1][col-1]
        return dp

    def sumRegion(self, row1, col1, row2, col2):
        if self.matrix:
            row1 += 1
            col1 += 1
            row2 += 1
            col2 += 1
            return self.dp_matrix[row2][col2] - self.dp_matrix[row1-1][col2] - \
                   self.dp_matrix[row2][col1-1] + self.dp_matrix[row1-1][col1-1]
        else:
            return 0

class TestNumMatrix(object):
    def test_from_vid(self):
        matrix = [
                  [2, 0, -3, 4],
                  [6, 3,  2, -1],
                  [5, 4,  7, 3],
                  [2, -6,  8, 1]
                ]
        obj = NumMatrix(matrix)
        assert obj.sumRegion(1, 1, 3, 2) == 18
        assert obj.sumRegion(0, 2, 3, 3) == 21

    def test_num_matrix(self):
        matrix = [
                  [3, 0, 1, 4, 2],
                  [5, 6, 3, 2, 1],
                  [1, 2, 0, 1, 5],
                  [4, 1, 0, 1, 7],
                  [1, 0, 3, 0, 5]
                ]
        obj = NumMatrix(matrix)
        assert obj.sumRegion(2, 1, 4, 3) == 8
        assert obj.sumRegion(1, 1, 2, 2) == 11
        assert obj.sumRegion(1, 2, 2, 4) == 12