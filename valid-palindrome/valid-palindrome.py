class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        string = []
        for i in s:
            if i.isalnum():
                string.append(i)
        
        print(string)
        
        if(len(string) <= 0):
            return True
        
        for i in range(len(string)/2):
            if string[i] != string[len(string)-1-i]:
                return False
        
        return True