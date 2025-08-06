class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
                
        freq_bucket = [[] for _ in range(len(nums))]
       
        for key in freq:
            freq_bucket[freq[key]-1].append(key)
        
        result = []
        for bucket in freq_bucket:
            result += bucket
        
        return result[-k:]
        
        
        