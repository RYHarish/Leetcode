# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node):
        # Push all the left children to the stack
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        :rtype: int
        """
        # Node at the top of the stack is the next smallest
        top_node = self.stack.pop()

        # If the node has a right child, do the same with that subtree
        if top_node.right:
            self._leftmost_inorder(top_node.right)

        return top_node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0