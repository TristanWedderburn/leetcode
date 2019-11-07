class Solution:
#   binary optimization
#     def singleNumber(self, nums: List[int]) -> int:
#         single = 0
        
#         for num in nums:
#             single^=num
#         return single

#       O(n) time and O(1) space solution
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        i, singleNum = 0,0
        
        while i < len(nums):
            if (i+1 < len(nums) and nums[i+1] == nums[i]):
                while (i+1 < len(nums) and nums[i+1] == nums[i]):
                    i+=1
                i+=1 
                continue
            singleNum = nums[i]
            i+=1
            
        return singleNum
        
