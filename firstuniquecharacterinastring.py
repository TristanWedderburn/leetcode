# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         alpha = [0]*26
        
#         for i in range(len(s)):
#             index = ord(s[i])-ord('a')
#             alpha[index]+=1
        
#         for j in range(len(s)):
#             index = ord(s[j])-ord('a')
#             if alpha[index]==1:
#                 return j
            
#         return -1

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:        
        occurences = Counter(s) #using Counter object to create dict of each letters occurrence in string
        
        for i,char in enumerate(s):
            if occurences[char] == 1: 
                return i
        return -1 #if empty string or no unique char
