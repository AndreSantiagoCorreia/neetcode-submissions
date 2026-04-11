class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            curr_len = len(s)
            res += str(curr_len) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i in range(len(s)):
            curr_str_len = ""
            while s[i] != "#":
                curr_str_len += s[i]
                i += 1
            curr_str_len = int(curr_str_len)
            next_start = i + curr_str_len + 1
            curr_str = s[i + 1 : next_start]
            res.append(curr_str)
            i = next_start
            # i=1, [i+1: i+curr_str_len+1] 3#eae5#andre

        return res