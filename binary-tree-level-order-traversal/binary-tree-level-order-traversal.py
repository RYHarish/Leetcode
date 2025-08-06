# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        queue = [root]
        result = []
        
        while queue:
            level_size = len(queue)
            level_node = []
            
            for _ in range(level_size):
                
                node = queue[0]
                del queue[0]
                level_node.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_node)
            
            
        
        return result