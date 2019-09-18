class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or (len(nums) ==1 and nums[0]!=target):
            return -1
        
        left = 0
        right = len(nums)
        
        while(left <= right):
            mid = left + (right-left)//2
            val = nums[mid]
            if val == target:
                return mid
            elif val > target:
                right = mid-1
            elif val < target:
                left = mid+1
                    
        return -1
