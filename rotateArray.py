class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         numsLen = len(nums)
#         rotated = [0]*numsLen
#         for i in range(numsLen):
#             index = (i+k)%numsLen
#             rotated[index] = nums[i]
            
#         for i in range(numsLen):
#             nums[i] = rotated[i]
            
#         # O(n) time and space
#         # can do this in O(1) space using cyclic replacements or by reversing whole array, then reversing first k and reversing last k
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums) #determine simplified k offset
        
        a = nums[::-1] #reverse nums to get back elements to the front
        b = a[0:k][::-1] #reverse first k elements
        c =  a[k:][::-1] #reverse other elements
        d = b+c
        
        for i in range(len(nums)): #modify nums in-place
            nums[i] = d[i]
