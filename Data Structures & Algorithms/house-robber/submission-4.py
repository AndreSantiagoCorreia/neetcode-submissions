class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        If we rob house[n]
        - we cannot rob house[n+1] and could have not robbed house[n-1]

        Approach: DP, optimized space
        """
        # Represent dp[i+1] and dp[i+2] initially out of the array bounds
        next_house = 0  # dp[i+1]
        two_houses_ahead = 0  # dp[i+2]
        
        # Iterate through the list backwards
        for num in reversed(nums):
            # Decision for the current house
            current = max(num + two_houses_ahead, next_house)
            
            # Shift the window to the left
            two_houses_ahead = next_house
            next_house = current
            
        return next_house
        
        """
        Approach: DP + DFS
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

        return dfs(0)


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