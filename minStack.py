# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []

#     def push(self, x: int) -> None:
#         if len(self.stack)==0:
#             self.stack.append((x,x))
#         else:
#             self.stack.append((x, min(x, self.stack[-1][1])))

#     def pop(self) -> None:
#         if len(self.stack)>0:
#             self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1][0] if len(self.stack)>0 else None

#     def getMin(self) -> int:
#         return self.stack[-1][1] if len(self.stack)>0 else None


# # Your MinStack object will be instantiated and called as such:
# # obj = MinStack()
# # obj.push(x)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_elem_set = []

    def push(self, val: int) -> None:
        if self.min_elem_set: # if values
            if val <= self.min_elem_set[-1]: # if less than last min, append
                self.min_elem_set.append(val)
        else: # no items, must be min
            self.min_elem_set.append(val)
        
        self.stack.append(val)

    def pop(self) -> None:
        if self.top() == self.min_elem_set[-1]: # pop min elements
            self.min_elem_set.pop()
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int: # Note: throws if no items
        if not self.min_elem_set:
            return None
        return self.min_elem_set[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
