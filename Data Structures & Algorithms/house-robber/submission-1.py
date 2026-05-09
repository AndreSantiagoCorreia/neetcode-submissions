class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        If we rob house[n]
        - we cannot rob house[n+1] and could have not robbed house[n-1]

        Approach: DP

        """
        n = len(nums)
        index_results = {}
        if n == 1:
            return nums[0]

        def dfs(index):
            if index >= n:
                return 0
            if index in index_results:
                return index_results[index]

            index_results[index] = max(nums[index] + dfs(index + 2), dfs(index + 1))  

            return index_results[index]      
             

        return max(dfs(0), dfs(1))


        """
        Approach: DFS -> O(n^2)
        1 2 3 4 5 6 7
        x   x     x 
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        def dfs(index):
            if index >= n:
                return 0

            return max(nums[index] + dfs(index + 2), dfs(index + 1))           
             

        return max(dfs(0), dfs(1))