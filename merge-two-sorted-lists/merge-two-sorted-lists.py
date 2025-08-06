# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        new_list = ListNode(0)
        head = new_list
        
        ptr1 = list1
        ptr2 = list2
        
        while list1 != None and list2 != None:
            
            if list1.val < list2.val:
                new_list.next = ListNode(list1.val) 
                new_list = new_list.next
                list1 = list1.next
                
            elif list2.val < list1.val:
                new_list.next = ListNode(list2.val) 
                new_list = new_list.next
                list2 = list2.next
                
            elif list1.val == list2.val:
                new_list.next = ListNode(list1.val)
                new_list = new_list.next
                new_list.next = ListNode(list1.val)
                new_list = new_list.next
                list2 = list2.next
                list1 = list1.next
                
        if list1 == None:
            new_list.next = list2
        else:
            new_list.next = list1
        
        
        return head.next

        
        