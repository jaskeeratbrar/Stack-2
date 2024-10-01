## T(C) -- O(n)
## S(c) -- O(n) ... asymptotic

class Solution:
    def isValid(self, s: str) -> bool:

        mapStore = {")":"(", "]":"[", "}":"{" }

        stack = []

        for i in s:

        ##  if our string character is a closing bracket
            if i in mapStore:


                if stack and stack[-1] == mapStore[i]:
                    stack.pop()
                
                ## to handle edge case, incase stack is of size 1 and string only contains
                ## closing paranthesis as its sole character

                else:
                    return False
            
            ## keep pushing opening paranthesis to our stack        
            else: stack.append(i)
        
        ## if len is zero, it means our paranthesis was valid
        if not stack: return True
        
