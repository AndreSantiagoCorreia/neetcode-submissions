# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: Min Heap
        - TC = O(n*logk), SC = O(k)
        - Push the head of each linked list into a min_heap, store it's reference
            then we can use it's .next to push back into the min_heap and 
            define it's .next to be the next popped node
        - This will work as the lists are sorted, that guarantees that we are 
            always comparing the min value across all k lists before 
            putting it into the resulting list
        - Stop whenever the heap is empty
        """
        min_heap = []
        counter = 0
        for k in range(len(lists)):
            node = lists[k]
            if node:
                heapq.heappush(min_heap, (node.val, counter, node))
                counter += 1
        
        res = ListNode()
        curr = res

        while min_heap:
            _, _, node = heapq.heappop(min_heap)
            curr.next = node
            if node.next:
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1
            curr = node

        return res.next