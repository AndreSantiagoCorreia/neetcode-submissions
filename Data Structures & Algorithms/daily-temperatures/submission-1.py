class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Monotonic stack:
        - we populate the stack with indicies, if temperatures are in descending order
        - once we find a non-descending, we can pop elements from the stack and calculate results
        """
        n = len(temperatures)
        stack = [] 
        results = [0] * n

        for i in range(n):
            curr_temp = temperatures[i]
            while stack and temperatures[stack[-1]] < curr_temp:
                index = stack.pop()
                results[index] = i - index

            stack.append(i)

        return results