class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        AAABABB, k = 1
        AAABA.. res = 5 ***
        ...BABB res = 4


        AAABABB, k = 2
        a=1
        a=2
        a=3
        a=3,b=1
        a=4,b=1
        a=4,b=2
        a=3,b=2
        a=2,b=2
        a=2,b=3
        """
        res = 0
        l, r = 0, 0
        maxF = 0
        frequencies = defaultdict(int)

        while r < len(s):
            # add char to the window
            frequencies[s[r]] += 1
            maxF = max(maxF, frequencies[s[r]])
            while (r - l + 1) - maxF > k:
                # remove left char from frequencies
                frequencies[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1

        return res
