class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        nums.sort()
        triplets = []
        length = len(nums)
        
        for i in range(length):
            if i >0 and nums[i] == nums[i-1]: continue
            left = i+1
            right = length-1
            
            while left < right:
                s = nums[i] + nums[left] +nums[right]
                if s <0: left+=1
                if s >0: right-=1
                if s == 0:
                    triplets.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]: left+=1
                    while left < right and nums[right] == nums[right-1]: right-=1
                    left+=1
                    right-=1
                    
        return triplets
                        
                    
        
