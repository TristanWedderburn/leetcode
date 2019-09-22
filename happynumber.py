class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set() # set of previous n values to verify if we are in a cycle
        
        while n!=1:
# sum digits of n 
            n = sum(int(digit) ** 2 for digit in str(n))
            if n in seen:
                return False
            else:
                seen.add(n) 
        return True
    
    
