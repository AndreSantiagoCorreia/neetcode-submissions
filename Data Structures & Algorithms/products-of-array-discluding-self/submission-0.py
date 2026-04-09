class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Approach: prefix sum.

        [x, y, z] -> [yz, xz, yz]
        Move right to left and keep productPrefixSum of all elements up to that point\
        [yz,z,1]
        Move left to right, use the prefixSum computed above and start storing results, 
            keep track of left to right product (used for computation)
        [1*yz, x*z, xy*1]
        """
        n = len(nums)
        prefix_sum = [0] * n
        curr_prod = 1
        for i in reversed(range(n)):
            prefix_sum[i] = curr_prod
            curr_prod *= nums[i]

        
        results = [0] * n
        curr_prod = 1
        for j in range(n):
            results[j] = curr_prod * prefix_sum[j]
            curr_prod *= nums[j]
        
        return results