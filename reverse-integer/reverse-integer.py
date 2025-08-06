class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = -1 if x < 0 else 1
        unsigned = abs(x)
        
        answer = 0
        length = 0
        y = unsigned
        
        while y>0:
            y = y/10
            length = length + 1 
        
        while unsigned>0:
            i = unsigned%10
            answer = answer + i*(10**(length-1))
            length -= 1
            unsigned = unsigned/10

        answer = answer*sign
        
        if answer >= -1*(2**31) and answer <= (2**31)-1:
            return answer
        
        return 0