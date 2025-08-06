class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        track = {}
        for i, num in enumerate(nums):
            if num in track:
                return [track[num], i]
            track[target - num] = i
            