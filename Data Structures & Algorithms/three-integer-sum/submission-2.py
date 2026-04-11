class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        We need to find 3 nums that sums up to 0.
        If we fix a number, say nums[i], our equation becomes:
        -> nums[j] + nums[k] = -nums[i]
        [-1,0,1,2,-1,-4]
        We can sort the array further:
        [-4,-1,-1,0,1,2]
        i    j        k  -> here we can increment j until it reaches k, and we wont find any result (nums[j] + nums[k] < -nums[i])
            i  j      k  -> here we found a result! (nums[j] + nums[k] = -nums[i])
                         -> we can skip setting nums[i] = -1 again as it might create duplicates (already covered previously)
                  i j k  -> here we can decrement k until i reaches j, and we wont find any result (nums[j] + nums[k] > -nums[i])
        """
        res = []
        nums.sort() # sort the array
        length = len(nums)
        i, j, k = 0, 1, (length - 1)
        
        while i <= (length - 3):
            # Otimização: se o menor número for > 0, impossível somar 0
            if nums[i] > 0:
                break
                
            target = -nums[i]
            curr_sum = nums[j] + nums[k]

            while j < k:
                curr_sum = nums[j] + nums[k]
                if curr_sum < target:
                    j += 1
                elif curr_sum > target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    # 1. Movimentar os ponteiros para sair do loop
                    j += 1
                    k -= 1
                    # 2. Pular duplicatas para 'j' e 'k' para não repetir o mesmo trio
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            
            i += 1
            while i <= (length - 3) and nums[i-1] == nums[i]:
                i += 1
            
            j = i + 1
            k = length - 1
            
        return res