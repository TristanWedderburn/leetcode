class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        minInt = -(2)**31
        maxInt = (2**31)-1
#       flag to determine whether we should expect numbers now i.e we have seen a sign or an number already within the string
        isNumber = False
        atoi = 0
        sign = 1
        i = 0
        
        while(i< len(str)):
            if not isNumber and str[i] == ' ':
#               remove whitespace
                pass
            elif not isNumber and str[i] == '-':
                sign = -1
                isNumber = True
            elif not isNumber and str[i] == '+':
                sign = 1
                isNumber = True
            elif str[i].isdigit():
                atoi = atoi*10 + int(str[i])
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
                
