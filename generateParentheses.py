class Solution(object):
    def __init__(self):
        self.combos=set()
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        self.permutate('',n,0,0)
        return self.combos
        
    def permutate(self,current,n,left,right):
        if len(current) == 2*n:
            self.combos.add(current)
            return
        if left <n: #must have <= n open brackets
            self.permutate(current+'(', n, left+1, right)
        if right < left: #can only add closing bracket if there are more open brackets
            self.permutate(current+')', n, left, right+1)
