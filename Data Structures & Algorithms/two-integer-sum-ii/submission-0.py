class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        NOTE: Your solution must use only constant extra space.
        Hence, we cannot add all compliments to a set.
        2pointer approach:
        -- Start with left and right pointers
        --- each time compute their sum
        ---- if sum is too big, decrease R
        ---- if sum is too small, increase L
        ---- if sum matches, return [L, R] 
        """
        result = []
        l, r = 0, len(numbers) - 1

        while l < r:
            two_sum = numbers[l] + numbers[r]
            if two_sum == target:
                return [l + 1, r + 1]
            elif two_sum > target:
                r -= 1
            else:
                l += 1

        return result