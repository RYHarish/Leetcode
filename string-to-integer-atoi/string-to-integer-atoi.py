class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        int_min = -1*(2**31)
        int_max = (2**31) - 1
        
        first = 0
        sign = 1
        integer = []
        answer = 0
        i = 0
        
        for i, char in enumerate(s):
            if not char.isnumeric() and char not in ["-", "+", " "]:
                return 0
            if char in ["-", "+"]:
                if char == "-":
                    sign = -1
                break
            elif char.isnumeric() and char !=0:
                i = i-1
                break
        
        
        i+=1
        while i < len(s):
            if not s[i].isnumeric():
                return 0
            elif s[i] != "0":
                integer.append(s[i])
                break
            i+=1

        i+=1
        while i<len(s):
            if s[i].isnumeric():
                integer.append(s[i])
                i+=1
            else:
                break
        
        length = len(integer)
        for i in integer:
            answer = answer + int(i)*(10**(length-1))
            length -= 1
        
        if answer*sign > int_max:
            return int_max
        elif answer*sign < int_min:
            return int_min
        else:
            return (answer*sign)
            
        
                
                
                