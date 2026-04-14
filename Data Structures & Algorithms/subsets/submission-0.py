class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr_subset = []
        n = len(nums)

        def dfs(index):
            if index == n:
                res.append(list(curr_subset))
                return

            curr_subset.append(nums[index])
            dfs(index + 1)
            curr_subset.pop()
            dfs(index + 1)

        dfs(0)
        return res