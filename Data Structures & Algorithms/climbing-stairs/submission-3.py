class Solution:
    def climbStairs(self, n: int) -> int:
        """
        n = 1
        - there is one way (from 0 to 1)

        n = 2
        - there are two ways (from 0 to 2 or from 1 to 2)

        n = 3
        - 0->1->2->3
        - 0->1->3
        - 0->2->3

        n = 4
        - 0->1->2->3->4
        - 0->1->2->4
        - 0->1->3->4
        - 0->2->3->4
        - 0->2->4
        """
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one