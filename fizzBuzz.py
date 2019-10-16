class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n or n==0:
            return []
        
        result = ['']*n #preallocated array of size n instead of appending
        
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                result[i-1] ='FizzBuzz'
            elif i%5==0:
                 result[i-1]='Buzz'
            elif i%3==0:
                 result[i-1] = 'Fizz'
            else:
                result[i-1]= str(i)
                
        return result
                
