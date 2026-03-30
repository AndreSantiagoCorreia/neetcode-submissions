class Solution:
    def binary_search(self, arr: List[int], target: int) -> int:
        lp, rp = 0, len(arr)-1

        while lp <= rp:
            middle = (rp - lp) // 2 + lp
            if arr[middle] == target:
                return middle
            if arr[middle] < target:
                lp = middle + 1
            else:
                rp = middle - 1
        return -1
    
    def col_binary_search(self, arr: List[int], target: int) -> int:
        lp, rp = 0, len(arr)-1

        while lp <= rp:
            middle = (rp - lp) // 2 + lp
            if arr[middle] == target:
                return middle # lucky!
            if arr[middle] < target:
                # if the next row starts with an element > target, this is the row we can search for
                if (middle + 1) < len(arr) and arr[middle + 1] > target:
                    return middle 
                lp = middle + 1
            else:
                rp = middle - 1
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        
        intuition:
        - perform binary search in the columns, to find the approriate row where target would be encountered
            this means if target = 10, it would be in row starting 7 as the next one starts at 11.
        -- having a fixed row, perform a simple binary search in it, return -1 if not found
        """
        # Extract the first element (index 0) from every row
        first_column = [row[0] for row in matrix]
        col = self.col_binary_search(first_column, target)
        return False if self.binary_search(matrix[col], target) == -1 else True
        