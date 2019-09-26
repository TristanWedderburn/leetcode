class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
#       add elements from num2 to remaining space in nums1
        for i, num in enumerate(nums2):
            nums1[i+m] = nums2[i]
        
        return nums1.sort()
        
