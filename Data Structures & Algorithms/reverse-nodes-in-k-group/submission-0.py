# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Apporach: Find kth node, and reverse group iteratively
        - TC = O(n), SC = O(1)
        """
        # Nó dummy para facilitar a manipulação do início da lista
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy
        
        while True:
            # 1. Encontra o k-ésimo nó do grupo atual
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next # Salva o início do próximo grupo
            
            # 2. Inverte o grupo atual de nós
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # 3. Atualiza as conexões do grupo invertido com o restante da lista
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            
        return dummy.next
    
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

        """
        Approach: Stack
        - TC = O(n), SC = O(n)
        1->2->3->4->5->6 / k = 4

        Iterate through the list and push each node to the stack.
        We can use a stack to store until it is len(k),
            once it reaches that, we will pop each node and 
            add it to the beginning, reconstructing the list.
        At the very end, iterate through the stack and append any "leftovers"  
        """
        stack = []
        res = ListNode()
        curr = res

        while head:
            stack.append(head)
            head = head.next

            if len(stack) == k:
                while stack:
                    curr.next = stack.pop()
                    curr = curr.next
                curr.next = None

        if len(stack):
            curr.next = stack[0]

        return res.next