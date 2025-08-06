# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        
        current = head
        length = 0
        while current != None:
            length += 1
            current = current.next
            
        current = head
        i = 0
        while i <= length/2:
            slow = current
            current = current.next
            i += 1
        
        while current != None:
            fast = current.next
            current.next = slow
            slow = current 
            current = fast 
        
        i = 0
        while i < length/2:
            if(head.val == slow.val):
                head = head.next
                slow = slow.next
                i+=1
                continue
            else:
                return False
        
        return True

            
        
        
        
            