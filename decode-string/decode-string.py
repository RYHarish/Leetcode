class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
    
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                decoded_string = []
                while stack and stack[-1] != '[':
                    decoded_string.append(stack.pop())
                stack.pop()
           
                k = []
                while stack and stack[-1].isdigit():
                    k.append(stack.pop())
                repeat_count = int(''.join(reversed(k)))
            
                repeated = ''.join(reversed(decoded_string)) * repeat_count
                stack.extend(repeated)
                print(stack)
    
        return ''.join(stack)