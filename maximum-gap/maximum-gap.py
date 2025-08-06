class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        
        nums = sorted(nums)
        
        max_diff = 0
        prev = nums[0]
        for num in nums:
            if (num - prev) > max_diff:
                max_diff = num - prev
            prev = num
                
        return max_diff
            