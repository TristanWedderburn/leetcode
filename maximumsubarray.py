class Solution(object):
#     recursive solution O(n) time and space
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         return self.sum(nums, 1,nums[0],nums[0])

#     def sum(self, nums, index, prevSum, maxSum):
#         if index == len(nums):
#             return prevSum
#         else:
#             if nums[index] > prevSum + nums[index]: #drop and start new sum
#                 currentSum = self.sum(nums, index+1, nums[index], maxSum)
#             elif index+1 < len(nums): #add val to currentSum
#                 currentSum = self.sum(nums, index+1, prevSum+nums[index], maxSum)
#             return max(maxSum, prevSum, currentSum)

# iterative solution --> O(n) time and O(1) space
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        currentSum = nums[0]
        maxSum = nums[0]
        
        for i in range(1, len(nums)):
            val = nums[i]
            
            # if val > currentSum + val:
            #     currentSum = val
            # else:
            #     currentSum+=val
            
            currentSum = max(currentSum+val, val) #can simplify to just max of currentSum + val or val to implement above logic
            maxSum = max(maxSum, currentSum)
            
        return maxSum
