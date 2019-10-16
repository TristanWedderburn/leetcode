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
            #add string to result index if applicable
            if i%3==0:
                result[i-1]+='Fizz'
            if i%5==0:
                result[i-1]+='Buzz'
            if not result[i-1]: #if ''
                result[i-1]+= str(i)
                
        return result
                
