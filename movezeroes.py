class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        
        if length <= 1:
            return
        
        search = 0 #search
        lastNum = 0 #last non-zero val
        zeroes = 0 #track zeroes
        
        while(search < length):
            if nums[search] != 0:
                nums[lastNum] = nums[search]
                lastNum+=1
            else:
                zeroes+=1
            search+=1
        
        for i in range(length-zeroes, length, 1):
            nums[i]=0
