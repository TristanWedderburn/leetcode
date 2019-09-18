class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nearbyHash = {}
        for i, c in enumerate(nums):
            if c in nearbyHash and abs(i - nearbyHash[c])<=k:
                return True
            else:
                nearbyHash[c] = i
            
        return False
