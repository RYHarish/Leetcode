class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        one = 0 
        two = 0
        
        if len(needle) > len(haystack):
            return -1
        
        while one<len(haystack):
            two = 0
            
            if (len(haystack)-one) < len(needle):
                return -1
            
            if haystack[one] == needle[two]:
                while two < len(needle):
                    if two == len(needle) -1 and needle[two] == haystack[one+two]:
                        return one
                    elif needle[two] == haystack[one+two]:
                        two += 1
                    else:
                        break
            one+=1
        
        return -1