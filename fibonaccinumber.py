class Solution:
    def fib(self, N: int) -> int:
        if(N==0):
            return 0
        if(N==1):
            return 1
        a=0
        b=1
        for i in range(2,N):
            c=a+b
            a=b
            b=c
        return a+b
