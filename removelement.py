class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        search = 0
        
        while(search < length):
            if nums[search] == val:
                nums[search] = nums[length-1]
                length-=1
            else:
                search+=1
        
        return length
