## T(C) -- O(n)
## S(c) -- O(n) ... asymptotic

class Solution:
    def isValid(self, s: str) -> bool:

        mapTracker = {"]" : "[", "}" : "{", ")" : "(" }

        stack = []

        for i in s:

            if stack and i in mapTracker:
                if stack[-1] == mapTracker[i]:
                    stack.pop()
                else:
                    return False

            else: stack.append(i)
        
        if not stack: return True
