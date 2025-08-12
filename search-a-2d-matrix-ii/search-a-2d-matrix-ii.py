class Solution(object):
    def searchMatrix(self, matrix, target):
        
        if not matrix or not matrix[0]:
            return False

        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0] == target

        m, n = len(matrix), len(matrix[0])
        mid_row, mid_col = m // 2, n // 2
        pivot = matrix[mid_row][mid_col]

        if pivot == target:
            return True

        if pivot > target:
            return (
                self.searchMatrix([row[:mid_col] for row in matrix[:mid_row]], target) or  
                self.searchMatrix([row[mid_col:] for row in matrix[:mid_row]], target) or  
                self.searchMatrix([row[:mid_col] for row in matrix[mid_row:]], target)     
            )
        else:
            return (
                self.searchMatrix([row[mid_col:] for row in matrix[mid_row:]], target) or  
                self.searchMatrix([row[:mid_col] for row in matrix[mid_row:]], target) or  
                self.searchMatrix([row[mid_col:] for row in matrix[:mid_row]], target)     
            )
