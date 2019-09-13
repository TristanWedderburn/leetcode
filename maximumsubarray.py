class Solution:
#     O(n^2) time
# 
#     def maxSubArray(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
       
#         maxVal = nums[0]
        
#         for i in range(len(nums)):
#             dist = len(nums)-i
#             val = 0
#             for j in range(dist):
#                 val += nums[i+j]
#                 if val > maxVal:
#                     maxVal = val
                    
#         return maxVal

#     O(n) time
#     compare whether to add value at new index to subarray or scrap past max and start new max subarray at new index
# 
      def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        curSum = maxSum = nums[0]
        for i in range(1,len(nums)):
            val = nums[i]
            curSum = max(val, curSum+val)
            maxSum = max(maxSum, curSum)
            
        return maxSum
