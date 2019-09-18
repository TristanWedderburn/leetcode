class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
# find bigger list
# store count in hash table
# decrement count and append to array when encountered
        if not nums1 or not nums2:
            return []

        counter = {}
        intersection = []

        if len(nums1) >= len(nums2):
            bigger = nums1
            smaller = nums2
        else:
            bigger = nums2
            smaller = nums1

        for big in bigger:
            if big in counter:
                counter[big]+=1
            else:
                counter[big]=1

        for small in smaller:
            if small in counter:
                counter[small]-=1
                if counter[small] == 0:
                    del counter[small]
                intersection.append(small)

        return intersection
