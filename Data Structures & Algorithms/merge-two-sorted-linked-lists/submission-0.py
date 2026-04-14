# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
                1 -> 2 -> 4
                h
                1 -> 3 -> 5
                p
        dummy-> 
        if h.val <= p.val, we will append h and move
        Otherwise, we will append p and move
        dummy-> 1
        dummy-> 1 -> 1
        dummy-> 1 -> 1 -> 2
        dummy-> 1 -> 1 -> 2 -> 3
        dummy-> 1 -> 1 -> 2 -> 3 -> 4
        dummy-> 1 -> 1 -> 2 -> 3 -> 4 -> 5
        """
        dummy = ListNode()
        curr = dummy
        # while we are not done with one of the lists:
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next # move list1 further
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next

        # if one list is bigger than another, we might have remainder elements
        while list1:
            curr.next = list1
            curr = list1
            list1 = list1.next
        
        while list2:
            curr.next = list2
            curr = list2
            list2 = list2.next

        return dummy.next