class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'}':'{', ']':'[',')':'('}
        for bracket in s:
            if bracket in brackets:
                if len(stack) == 0 or stack.pop() != brackets[bracket]:
                    return False
            else:
                stack.append(bracket)
        return True if len(stack) == 0 else False
