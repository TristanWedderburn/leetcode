class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
#         conditions force specific solution
#           in-place with O(1) extra memory

        if not nums:
            return 0
        
        unique = 0
        nextUnique = 0
        
        while nextUnique < len(nums):
            val = nums[nextUnique]
            nums[unique] = val
            unique += 1
            
            while nextUnique < len(nums) and nums[nextUnique] == val:
                nextUnique+=1
        
        return unique
