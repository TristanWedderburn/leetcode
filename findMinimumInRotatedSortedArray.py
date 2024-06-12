class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left < right, left half starting at mid
        # left > right, right half starting at mid
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2 # Note; calc mid like this to avoid int out of range
            # check if the mid is greater than or equal to right. If so, value must be in right half based on rotation
            if nums[mid] > nums[right]:
                left = mid + 1
            else: # value must be in left half based on rotation
                right = mid
            
        return nums[left]
