class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = list(heights)
        
        has_swaped = True
        while has_swaped:
            has_swaped = False
            for i in range(len(expected) - 1):
                if expected[i] > expected[i+1]:
                    expected[i], expected[i+1] = expected[i+1], expected[i]
                    has_swaped = True
        
        count = 0 
        
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                count += 1
        
        return count
            
        