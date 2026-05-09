class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        3   4   5   6   1   2
        L       m           R
        nums[l] > nums[r] (means it's rotated)
        l = m
                l       m   r       
        nums[l] > nums[r] (means it's rotated)
        l = m
                        l   r
        nums[l] < nums[r] (means we found the inflection point)

        6   1   2   3   4   5
        L       m           R
        nums[l] > nums[r] (means it's rotated)
        l = m
                l       m   r       
        nums[l] > nums[r] (means it's rotated)
        l = m
                        l   r
        nums[l] < nums[r] (means we found the inflection point)

        - Now we have two sorted arrays
        --1: [0, l-1]
        --2: [l, r]
        First, evaluate which array we should proceed with Binary Search
        - Is target within (1) or (2)?
        Perform Binary Search on previous answered array
        """
        if not nums:
            return -1
            
        # PASS 1: Find the index of the pivot (the minimum element)
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1  # Pivot is in the right half
            else:
                r = m      # Pivot is at m or in the left half
                
        pivot = l
        
        # PASS 2: Determine which sorted subarray contains the target
        l, r = 0, len(nums) - 1
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot      # Search in the right sorted subarray
        else:
            r = pivot - 1  # Search in the left sorted subarray
            
        # Standard Binary Search
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
                
        return -1
        
