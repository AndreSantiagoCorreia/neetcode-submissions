class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        NOTE: nums of unique integers
        We need to manage a set to know which entry was used
        """
        res = []
        curr_perm = []
        used = set()
        n = len(nums)

        def dfs():
            if len(curr_perm) == n:
                res.append(curr_perm[:])
                return
            
            # for each index, we can decide to append it or not
            for i in range(n):
                if nums[i] in used:
                    continue
                
                used.add(nums[i])
                curr_perm.append(nums[i])
                dfs()

                used.remove(nums[i])
                curr_perm.pop()

        dfs()
        return res