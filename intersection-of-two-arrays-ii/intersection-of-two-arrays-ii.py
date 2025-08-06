class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        if len(nums1) > len(nums2):
            for num in nums2:
                if num in nums1:
                    nums1.remove(num)
                    result.append(num)
            return result
        else:
            for num in nums1:
                if num in nums2:
                    nums2.remove(num)
                    result.append(num)
                    
            return result