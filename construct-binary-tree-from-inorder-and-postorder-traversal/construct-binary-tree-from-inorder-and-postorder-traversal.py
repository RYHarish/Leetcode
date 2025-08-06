# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder or not postorder:
            return None
        
        inorder_index_map = {value: idx for idx, value in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            root_val = postorder[self.post_idx]
            root = TreeNode(root_val)

            index = inorder_index_map[root_val]
            self.post_idx -= 1

            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)

            return root

        return helper(0, len(inorder) - 1)
            