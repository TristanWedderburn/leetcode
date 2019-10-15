class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        numsLen = len(nums)
        rotated = [0]*numsLen
        for i in range(numsLen):
            index = (i+k)%numsLen
            rotated[index] = nums[i]
            
        for i in range(numsLen):
            nums[i] = rotated[i]
            
        # O(n) time and space
        # can do this in O(1) space using cyclic replacements or by reversing whole array, then reversing first k and reversing last k
         
