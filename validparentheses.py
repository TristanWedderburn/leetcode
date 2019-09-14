class Solution:
    def isValid(self, s: str) -> bool:
        #can implement using a stack and popping off of the stack when encountering a closed bracket
        bracket_stack = []
        
        for bracket in s:
#             check for empty stack before popping
            if (bracket == '}' or bracket == ']' or bracket == ')') and len(bracket_stack) > 0:
                check_open_bracket = bracket_stack.pop(-1)
                if bracket == ')' and check_open_bracket != '(':
                    return False
                if bracket == '}' and check_open_bracket != '{':
                    return False
                if bracket == ']' and check_open_bracket != '[':
                    return False
            else:
                bracket_stack.append(bracket)
#                 to be valid, all opening brackets must have closing brackets
        return True if len(bracket_stack) == 0 else False
