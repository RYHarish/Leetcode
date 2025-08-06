"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        current_level_start = root
        while current_level_start and current_level_start.left:
            node = current_level_start
            while node:
                
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left

                node = node.next
            current_level_start = current_level_start.left
    
        return root