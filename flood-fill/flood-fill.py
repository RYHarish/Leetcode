class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        true_color = image[sr][sc]
        
        if true_color == color:
            return image
        
        row, col = len(image), len(image[0])
    
        def dfs(r,c):
            if r >= row or c >= col or r < 0 or c < 0 or image[r][c] != true_color:
                return
            
            image[r][c] = color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        dfs(sr,sc)
        return image