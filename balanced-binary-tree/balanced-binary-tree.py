# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def height_and_balance(node):

            if node is None:
                return 0, True
            
            left_height, left_balanced = height_and_balance(node.left)
            right_height, right_balanced = height_and_balance(node.right)
            
            if not left_balanced or not right_balanced:
                return 0, False
            if abs(left_height - right_height) > 1:
                return 0, False

        
            return 1 + max(left_height, right_height), True

    

   

        _, balanced = height_and_balance(root)

        return balanced
    
    