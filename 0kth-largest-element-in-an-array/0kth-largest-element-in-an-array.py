class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        top = self.heap[0]
        # Move last element to top and heapify down
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return top

    def top(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self._heapify_down(smallest)

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = MinHeap()
        for num in nums:
            heap.push(num)
            if heap.size() > k:
                heap.pop()
            
        return heap.top()