class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        To compare each string if they are anagrams, we can first check:
        - their size matches
        then we can check:
        - if they contain the same letters
        To check that, we can either iterate each but that is not optimal, would give n^2 efficiency.
        Sorting is a better option n*logn (car -> acr, arc -> acr)
        
        To group then, we should mantain a set or map with their sorted key, and index in result array
        """
        dic = {}
        res = []

        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string in dic:
               idx = dic[sorted_string]
               res[idx].append(s)
            else:
                dic[sorted_string] = len(res)
                res.append([s])

        return res
