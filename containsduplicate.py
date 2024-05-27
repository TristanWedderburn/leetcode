class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # # sort
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if (nums[i] == nums[i+1]):
        #         return True
        # return False
        
        # use set
        unique_set = set()
        for num in nums:
            if num in unique_set:
                return True
            unique_set.add(num)
        return False
