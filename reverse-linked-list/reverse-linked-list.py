# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        fast = None
        slow = None
        
        while current != None:
            fast = current.next
            current.next = slow
            slow = current
            current = fast
            
        return slow