class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqueSet = set()
        for num in nums:
            if num in uniqueSet:
                return True
            else:
                uniqueSet.add(num)
        return False
