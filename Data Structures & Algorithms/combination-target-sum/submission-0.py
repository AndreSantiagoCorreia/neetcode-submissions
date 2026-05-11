class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset, curr_sum):
            if curr_sum == target: 
                res.append(subset.copy()) 
                return
            if i >= len(nums) or curr_sum > target:
                return
            
            subset.append(nums[i])
            dfs(i, subset, curr_sum + nums[i])
            subset.pop()
            dfs(i+1, subset, curr_sum)
        
        dfs(0, [], 0)
        return res