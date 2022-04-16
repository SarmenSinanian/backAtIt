class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            rowSet = set([])
            for j in range(len(matrix[0])):
                rowSet.add(matrix[i][j])
            if len(rowSet) != len(matrix[0]):
                return False
        for j in range(len(matrix[0])):
            colSet = set([])
            for r in range(len(matrix)):
                colSet.add(matrix[r][j])
            if len(colSet) != len(matrix):
                return False
        return True
