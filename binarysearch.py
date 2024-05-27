class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left and right pointers
        # if greater than mid, left is mid + 1
        # if less than mid, right is mid - 1
        # if value found, return true
        # stop at left > right

        left = 0
        right = len(nums) - 1

        while (left <= right):
            mid = (left + right) // 2 # checking middle of binary search
            
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target): # left tree
                right = mid - 1
                continue
            else: # right tree
                left = mid + 1
                continue

        return -1
 
