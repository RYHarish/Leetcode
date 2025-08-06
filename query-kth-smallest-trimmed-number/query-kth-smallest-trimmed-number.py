class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for k, trims in queries:
            trimmed = [(num[-trims:], i) for i, num in enumerate(nums)]
            trimmed.sort()
            res.append(trimmed[k-1][1])
        
        return res