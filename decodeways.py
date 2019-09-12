class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [0]*(len(s)+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,len(s)+1):
            a = int(s[i-1:i])
            b = int(s[i-2:i])
            if a >= 1:
                dp[i]+=dp[i-1]
            if (b >=10 and b <=26):
                dp[i]+=dp[i-2]
        return dp[len(s)]
