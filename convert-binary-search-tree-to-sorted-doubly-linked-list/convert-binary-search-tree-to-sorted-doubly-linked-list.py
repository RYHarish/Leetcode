"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return root
        
        nodes = []
        
        def divide(root):
            if root == None:
                return
            divide(root.left)
            nodes.append(root)
            divide(root.right)
        divide(root)
        
        
        
        if len(nodes) == 1:
            nodes[0].right = nodes[0]
            nodes[0].left = nodes[0]
            return nodes[0]
        
        nodes[0].right = nodes[1]
        nodes[0].left = nodes[-1]
        nodes[-1].right = nodes[0]
        nodes[-1].left = nodes[len(nodes)-2]
        
        for i in range(1, len(nodes)-1):
            nodes[i].right = nodes[i+1]
            nodes[i].left = nodes[i-1]
        
        return nodes[0]