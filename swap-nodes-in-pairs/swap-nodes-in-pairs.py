# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def swap(head):
            if head == None or head.next == None:
                return head
            
            temp = head.next
            head.next = head.next.next
            temp.next = head
            temp.next.next = swap(temp.next.next)
            
            return temp
        
        return swap(head)