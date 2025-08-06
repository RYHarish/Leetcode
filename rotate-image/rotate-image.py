class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """ 
        
        def rev_row(mat, row, n):
            j = 0
            while j<n/2:
                mat[row][j], mat[row][n-j-1] = mat[row][n-j-1], mat[row][j]
                j+=1
            
        n = len(matrix)
        
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            rev_row(matrix, i, n)
            