'''
2019/3/1
hsvnlu
runtime: 48ms 93.76%
memory: 17.5MB 5%
'''

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        row, column = len(matrix), len(matrix[0])
        row_rest, col_rest = 0, column - 1
        while row_rest < row and col_rest > -1:
            if target > matrix[row_rest][col_rest]:
                row_rest += 1
            elif target < matrix[row_rest][col_rest]:
                col_rest -= 1
            else: return True
        return False
