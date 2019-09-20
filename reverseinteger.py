class Solution:
    def reverse(self, x: int) -> int:
        reversed = 0
        sign = 1 if x >=0 else -1
        x = abs(x)
        
        while x > 0:
            val = x % 10
            x = x // 10
            reversed*=10 #new place available
            reversed+= val #add last digit from x to front of reversed)
            if (reversed > 2**31-1 or reversed < -2**31):
                return 0

        return reversed*sign 
        
