class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        lo, hi = min(arr), max(arr)
        width = hi - lo + 1          

        present = [False] * width
        for v in arr:
            present[v - lo] = True

        prev = None
        min_gap = float('inf')
        for i, seen in enumerate(present):
            if not seen:
                continue
            if prev is not None:
                min_gap = min(min_gap, i - prev)
            prev = i

        prev = None
        answer = []
        for i, seen in enumerate(present):
            if not seen:
                continue
            if prev is not None and i - prev == min_gap:
                a = lo + prev
                b = lo + i
                answer.append([a, b])  
            prev = i

        return answer