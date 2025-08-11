class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def kth(k, n):
            if n == 0:
                return 0
            
            if k%2 == 0 and kth(k//2, n-1) == 0:
                return 0
            elif k%2 == 1 and kth(k//2, n-1) == 0:
                return 1
            elif k%2 == 0 and kth(k//2, n-1) == 1:
                return 1
            elif k%2 == 1 and kth(k//2, n-1) == 1:
                return 0
            
        return kth(k-1, n-1)