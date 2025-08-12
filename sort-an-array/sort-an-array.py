class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        
        pivot = len(nums) // 2
        left_list = self.sortArray(nums[:pivot])
        right_list = self.sortArray(nums[pivot:])
        
        return self.merge(left_list, right_list)
        
    def merge(self, left_list, right_list):
        res = []
        left_cursor = right_cursor = 0
        
        while left_cursor < len(left_list) and right_cursor < len(right_list):
            if left_list[left_cursor] < right_list[right_cursor]:
                res.append(left_list[left_cursor])
                left_cursor += 1
            else:
                res.append(right_list[right_cursor])
                right_cursor += 1
        
        res.extend(left_list[left_cursor:])
        res.extend(right_list[right_cursor:])
        
        return res
