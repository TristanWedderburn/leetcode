class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        minInt = -(2)**31
        maxInt = (2**31)-1
        isNumber = False #flag to determine whether we should expect numbers now i.e we have seen a sign or a number already within the string
        atoi = 0
        sign = 1
        i = 0
        
        while(i< len(str)):
            char = str[i]
            if not isNumber and char == ' ':
                pass
            elif not isNumber and char == '-':
                sign = -1
                isNumber = True
            elif not isNumber and char == '+':
                sign = 1
                isNumber = True
            elif char.isdigit():
                atoi*=10
                atoi+=int(char)
                isNumber = True
            else:
                break
            i+=1
        
        atoi = sign*atoi
        
        if atoi < minInt:
            return minInt
        elif atoi > maxInt:
            return maxInt
        else:
            return atoi
                
