class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums)==1:
            return 0
    
        biggest = nums[0]
        biggestIndex = 0
        
#      find max value
        for i in range(len(nums)):
            val = nums[i]
            if val >= biggest:
                biggest = val
                biggestIndex = i
                
#     compare it to other values
        for j in range(len(nums)):
            val = nums[j]
            if val != biggest and 2*val > biggest:
                return -1
            
        return biggestIndex
