# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None
        
        inorder_index_map = {value: idx for idx, value in enumerate(inorder)}
        self.pre_idx = 0
        
        def helper(in_left, in_right):
            
            if in_left > in_right:
                return None
            
            root_val = preorder[self.pre_idx]
            index = inorder_index_map[root_val]
            root = TreeNode(root_val)
            
            self.pre_idx += 1
            
            root.left = helper(in_left, index-1) 
            root.right = helper(index+1, in_right)
            
            return root
        
        return helper(0, len(preorder) -1)
            
            