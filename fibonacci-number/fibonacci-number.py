class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        
        def f(n):
            
            if n in cache:
                return cache[n]
            
            if n<2:
                return n
            else:
                res = f(n-1) + f(n-2)
            
            cache[n] = res
            return res
        
        return f(n)
            