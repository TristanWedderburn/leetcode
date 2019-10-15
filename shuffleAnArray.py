from random import choice

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.set = list(nums) # set to list
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.set #keep original set as it is much easier to generate random output than to reverse random output
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        copy = self.set[:] #make deep copy of original set
        shuffled = [0]*len(copy) #allocate new array for new set
        for i in range(len(copy)):
            shuffled[i] = choice(copy) # randomly choose element from set
            copy.remove(shuffled[i]) # remove chosen item from set to choose from
        return shuffled

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
