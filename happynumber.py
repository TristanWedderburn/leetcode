class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while(n!=1):
            if n in seen:
                return False
            else:
                seen.add(n)
            n = self.sumDigitSquares(n)
        return True
    
    def sumDigitSquares(self,n):
        sum = 0
        while(n!=0):
            digit =(n%10)**2
            sum+=digit
            n = n//10
        return sum
