class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         nums.sort()
#         for i in xrange(len(nums)):
#             if nums[i]!=i:
#                 return i
#         return i+1

        expectedSum = len(nums)*(len(nums)+1)/2 #formula to sum elements up to n
        actualSum = sum(nums)
        return expectedSum - actualSum
        
