class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isValid(node, low, high):
            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            
            return isValid(node.left, low, node.val) and isValid(node.right, node.val, high)

        return isValid(root, float('-inf'), float('inf'))
