class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #prime numbers are only divisible by themselves and 1
        #if we do a modulo of numbers up to n --> this is n*(n-m) where is input and (n-m) is each number as we go from 0 to m i.e O(n^2)
        
        if n <= 2:
            return 0
        
        #uses Sieve of Eratosthenes to generate list of primes
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in xrange(2, n):
            if primes[i] == True:
                for j in xrange(2, (n-1)//i+1): #(n-1)//i+1 is the upper bound of how many times we need to update values in primes list
                    primes[i*j] = False
        return sum(primes)
