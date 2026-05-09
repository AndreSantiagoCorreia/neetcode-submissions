# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        1 - 2 - 3 - 4 - 5 - 6 - 7 / n = 3
                        x
                    s               f

        5 / n = 1
    s       f
        """
        dummy = ListNode(0)
        dummy.next = head
        
        first = dummy
        second = dummy
        
        # Avança o primeiro ponteiro n + 1 passos
        for _ in range(n + 1):
            first = first.next
            
        # Move ambos até o primeiro ponteiro atingir o fim (None)
        while first:
            first = first.next
            second = second.next
            
        # Remove o n-ésimo nó a partir do fim
        second.next = second.next.next
        
        return dummy.next