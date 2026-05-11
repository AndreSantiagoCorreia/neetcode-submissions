class Solution:
    def isValid(self, s: str) -> bool:
        """
        push the string to the stack
        pop each parenthesis at a time
        for each open parenthesis found, decrement the closed_counter
        if there is an open parenthesis and no counter for that, return False
        """
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
