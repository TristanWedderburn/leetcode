class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack)==0:
            self.stack.append((x,x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self) -> None:
        if len(self.stack)>0:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if len(self.stack)>0 else None

    def getMin(self) -> int:
        return self.stack[-1][1] if len(self.stack)>0 else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
