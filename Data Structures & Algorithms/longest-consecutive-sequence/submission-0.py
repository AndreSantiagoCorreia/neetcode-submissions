class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        We want to find the longest consecutive sequence in an array of nums
        They can be in any order

        To do that, we could sort the array but that would take O(n*logn)
        We need O(n)
        We can add all nums to a set()
        Then, for each num we can check:
        - if it's +1 is in the set, we can skip it
        - if it's +1 is not in the set, we count all -1 until the end and store that result
            this means we are dealing with the "head" of the sequence.
        """
        s = set(nums)
        res = 0

        for n in nums:
            if n+1 not in s:
                curr_res = 1
                curr_num = n
                while curr_num - 1 in s:
                    curr_res += 1
                    curr_num -= 1
                res = max(res, curr_res)
        
        return res