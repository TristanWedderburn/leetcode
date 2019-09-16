class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        left = right = 0
        
        for i in range(1, len(nums)):
            right+=nums[i]
        
        if right == 0:
            return 0
        
        for j in range(1, len(nums)):
            left+=nums[j-1]
            right-=nums[j]
            if left == right:
                return j
            
        return -1
