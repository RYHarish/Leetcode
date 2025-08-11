class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        cache = {}
        
        def row(i, j):
            
            if (i,j) in cache:
                return cache[(i,j)]
            
            if j == 1 or j == i:
                return 1
            else:
                r = row(i-1,j) + row(i-1,j-1)
            
            cache[(i,j)] = r
            
            return r
            
        for j in range(1, rowIndex+2):
            result.append(row(rowIndex+1, j))
        
        return result