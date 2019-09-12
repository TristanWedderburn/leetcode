class Solution:

# top down w/o memoization

#    def climbStairs(self, n: int) -> int:
#       if (n==0 or n==1):
#         return 1
#       return self.climbStairs(n-1)+self.climbStairs(n-2)
        
# top down w/ memoization

#    def climbStairs(self, n: int) -> int:
#         memo = {0:1, 1:1}
#         return self.climbStairs_(n, memo)
    
#     def climbStairs_(self, n, memo):
#         if n in memo:
#             return memo[n]
#         memo[n] = self.climbStairs_(n-1, memo) + self.climbStairs_(n-2, memo)
#         return memo[n]

# bottom down w/ memoization

#    def climbStairs(self, n: int) -> int:
#       if (n==0 or n==1):
#          return 1
#       memo = {0:1,1:1}
#
#       for i in range(2,n):
#          memo[i] = memo[i-1]+memo[i-2]
#
#       return memo[n-1]+memo[n-2]
        
# bottom down w/ variables

    def climbStairs(self, n: int) -> int:
        if(n==0 or n==1):
            return 1
        a=1 #index 0
        b=1 #index 1
        for i in range(2,n):
            c=a+b #temp
            a=b #shifting a up 1
            b=c #shifting b up 1
        return a+b
    
