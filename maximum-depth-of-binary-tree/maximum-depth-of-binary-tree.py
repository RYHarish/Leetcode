# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    answer = 0
    def maxDepth(self, root, depth = 1):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """ 
        
        if root is None:
            return 0

        if(root.left == None and root.right == None):
            self.answer = max(self.answer, depth)
    
        self.maxDepth(root.left, depth+1)
        self.maxDepth(root.right, depth+1)
        
        return self.answer