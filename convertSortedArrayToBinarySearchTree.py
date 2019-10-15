# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        
        return self.pivot(nums, 0, len(nums))
        
    def pivot(self, nums, low, high):
        if low >= high:
            return None
        else:
            mid = low + (high-low)//2
            
            pivot = TreeNode(nums[mid])
            pivot.left = self.pivot(nums, low, mid)
            pivot.right = self.pivot(nums, mid+1, high)

            return pivot
