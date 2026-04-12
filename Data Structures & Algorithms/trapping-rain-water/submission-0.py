class Solution:
    def trap(self, height: List[int]) -> int:
        """
        For a fixed index:
        -> water = min(prefix[i], suffix[i]) - height[i]
        We need to store prefix and suffix maximums from each side of the array, 
            and for a given point we can calculate water trapped
        """
        n = len(height)
        prefix_array, suffix_array = [], [0] * n
        curr_max = 0
        for i in range(n):
            curr_max = max(curr_max, height[i])
            prefix_array.append(curr_max)

        curr_max = 0
        for j in reversed(range(n)):
            curr_max = max(curr_max, height[j])
            suffix_array[j] = curr_max

        total_water = 0
        for k in range(n):
            total_water += min(prefix_array[k], suffix_array[k]) - height[k]

        return total_water