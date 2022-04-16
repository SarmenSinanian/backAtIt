# An n x n matrix is valid if every row and every column
# contains all the integers from 1 to n (inclusive).
#
# Given an n x n integer matrix matrix, return true if
# the matrix is valid. Otherwise, return false.

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
