class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        longest = 1
        i=0
        while i < len(nums):
            current = 1
            while(i+1 < len(nums)):
                if(nums[i]+1 == nums[i+1]):
                    current+=1
                    i = i+1
                elif(nums[i] == nums[i+1]):
                    i = i+1
                else:
                    break
            longest = max(longest, current)
            i=i+1
        return longest
