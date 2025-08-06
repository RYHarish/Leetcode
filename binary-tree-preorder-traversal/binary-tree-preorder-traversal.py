# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    output = []
    def preorder(self, root):
            if root == None:
                return []
            self.output.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
            
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.output = []
        self.preorder(root)
        return self.output
            