class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s)<1:
            return 0
        if len(s) == 1:
            return 1
        
        bank = [0]*128
        left=0
        right=0
        maxSubstring=0
        
        while right < len(s): #update max incrementally
            val = s[right]
            index = ord(val)
            if bank[index] == 0: #if val is not in bank, mark as passed
                maxSubstring = max(maxSubstring, right-left+1)
                bank[index]=1
                right+=1 #check for next char to add
            else:
                bank[ord(s[left])]=0 #remove leftmost char from bank
                left+=1 #retry without leftmost char
        return maxSubstring