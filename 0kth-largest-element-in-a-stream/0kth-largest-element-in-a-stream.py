import heapq

class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        
        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.heap, val)
        
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)  # remove smallest
        
        return self.heap[0]  # kth largest
