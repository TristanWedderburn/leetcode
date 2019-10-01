class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        for token in tokens:
            if token == '+':
                second = int(ans.pop())
                first = int(ans.pop())
                ans.append(first+second)
            elif token == '-':
                second = int(ans.pop())
                first = int(ans.pop())
                ans.append(first-second)
            elif token == '/':
                second = int(ans.pop())
                first = int(ans.pop())
                ans.append(first/second)
            elif token == '*':
                second = int(ans.pop())
                first = int(ans.pop())
                ans.append(first*second)
            else:
                ans.append(token)
                            
        return int(ans.pop())
