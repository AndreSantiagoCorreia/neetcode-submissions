class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        the minCost of reaching index n is the min(cost n-1, cost n-2)
        """
        n = len(cost)
        first = cost[0]
        second = cost[1]

        for i in range(2, n):
            current = cost[i] + min(first, second)
            first = second
            second = current

        return min(first, second)