class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        odd-length Palindrome:
        - pick one center, then expand left and right pointers as both chars match and are within boundaries

        even-length Palindrome:
        - pick two indicies to start:
        -- left and right, then expand both as they match and are within boundaries
        """
        res = 0
        n = len(s)

        for i in range(n):
            # odd-length
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # even-length
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res