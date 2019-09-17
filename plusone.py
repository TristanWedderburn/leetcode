class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return None
        
        carry = 0
        val = digits[-1]
        val+=1
        digits[-1] = val
        
        if val == 10: #if we need to add a carry, pass it down into the array
            carry = val // 10
            digits[-1] = val %10
            for i in range(1, len(digits)): #traverse array from the back
                newVal = digits[len(digits)-i-1]
                newVal+=carry
                if newVal == 10: #pass on carry
                    digits[len(digits)-i-1] = newVal%10
                    carry = newVal // 10
                else: #just add carry to number
                    digits[len(digits)-i-1] = newVal
                    carry = 0
                
        if carry == 1:    #if there is a carry after traversing the whole array, add a new index in the front of the array
            newDigits = [carry]
            newDigits.extend(digits)
            digits = newDigits
            
        return digits
