class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while right > left:
            sum_val = numbers[left] + numbers[right]
            
            if (sum_val == target): # equals sum
                return [left + 1, right + 1]
            elif (sum_val > target): # larger than target
                right-=1
            else: # less than target
                left+=1
        
        return [-1, -1] # no solution found
     
