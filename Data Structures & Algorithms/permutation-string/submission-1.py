class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Constraints: Both strings only contain lowercase letters.
        Sliding window:
        First, we need to know how which chars and respective frequencies in s1.
        After that is built:
        We can the slide our right pointer through s2 and:
        - if we find a char that is not contained in s1:
            we can move left pointer up to a point where we create a valid window
        - if we find a char contained in s1:
            we decrement its frequency in our temporary array
        Once we have enough length, we can check for correctness and return early
        """
        len_s1 = len(s1)
        len_s2 = len(s2)
        char_freqs = [0] * 26

        for c in s1:
            char_freqs[ord(c) - ord('a')] += 1

        window_freqs = [0] * 26 
        lp, rp = 0, 0

        while rp < len_s2:
            curr_char = s2[rp]
            window_freqs[ord(curr_char) - ord('a')] += 1

            # if we added a char that is invalidates our window, we need to move our lp, until we have a valid window
            while lp <= rp and window_freqs[ord(curr_char) - ord('a')] > char_freqs[ord(curr_char) - ord('a')]:
                window_freqs[ord(s2[lp]) - ord('a')] -= 1
                lp += 1
            
            if (rp - lp + 1) == len_s1 and window_freqs == char_freqs: 
                return True 
            
            rp += 1
        
        return False