class Solution:
    def firstUniqChar(self, s: str) -> int:
        alpha = [0]*26
        
        for i in range(len(s)):
            index = ord(s[i])-ord('a')
            alpha[index]+=1
        
        for j in range(len(s)):
            index = ord(s[j])-ord('a')
            if alpha[index]==1:
                return j
            
        return -1
