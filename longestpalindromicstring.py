class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
    
        longest = ''
        for i in range(len(s)):
            odd = self.palindrome(s,i,i+2) #aba
            even = self.palindrome(s,i,i+1) #abba
            longest = max(longest, odd, even, key=len)
        return longest
    
    def palindrome(self, s, start, finish):
        while (start >= 0 and finish < len(s) and s[start] == s[finish]):
            start-=1;
            finish+=1;
        return s[start+1:finish]
