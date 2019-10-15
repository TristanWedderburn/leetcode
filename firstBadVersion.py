# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 1 #quick return if there are no versions
        
        low = 0
        high = n
        
        while low <= high: #less than or equal to so that we can narrow down the bounds to 1 element
            mid = low + (high-low)//2
            if isBadVersion(mid):
                if mid-1 >0:
                    if isBadVersion(mid-1):
                        high = mid
                    else:
                        return mid
                else:
                    return mid
            else:
                low = mid+1
        return 1
        
