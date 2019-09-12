class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for i in range(len(nums)):
            curr = nums[i]
            rem = target - curr
            if rem in found:
                return [found[rem],i]
            else:
                found[curr] = i
        return [-1,-1]
