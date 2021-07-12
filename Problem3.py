class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [] or len(matrix) == 0:
            return false
        
        m, n = len(matrix), len(matrix[0])
        row, col = 0,n-1
        
        while row < m and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        return False
