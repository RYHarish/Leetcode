class Solution(object):
    def climbStairs(self, n, memo={}):
        """
        :type n: int
        :rtype: int
        """
        if n in memo:
            return memo[n]
        if n == 0 or n == 1:
            return 1
        memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
        return memo[n]