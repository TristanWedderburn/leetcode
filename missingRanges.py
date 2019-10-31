class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            if upper == lower:
                return [str(lower)]
            return [str(lower)+'->'+str(upper)]

        ranges = []
        nums = [lower-1]+nums+[upper+1]  
            
        for i in range(1, len(nums)):
            if nums[i]!=nums[i-1]+1 and nums[i]!=nums[i-1]:
                range_upper = nums[i]-1
                range_lower = nums[i-1]+1
                if range_upper == range_lower:
                    ranges.append(str(range_lower))
                    continue
                ranges.append(str(range_lower)+'->'+str(range_upper))
        return ranges
