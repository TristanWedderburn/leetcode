class Solution(object):
    
    def __init__(self):
        self.combos = []
        self.keypad = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return self.combos
        
        self.permutate(digits, '',0)
        self.combos.sort()
        return self.combos
        
    def permutate(self, digits, current, next):
            if next == len(digits):
                self.combos.append(current)
                return
            
            digit = digits[next]
            choices = self.keypad[digit]
            for choice in choices:
                self.permutate(digits,current+choice, next+1)
