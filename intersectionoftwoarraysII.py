class Solution(object):
#     def intersect(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """

#       bigger or smaller list doesn' t matter because we are looking for the min of occurrences in both lists
#         counts = {}
#         res = []

#         for num in nums1:
#             counts[num] = counts.get(num, 0) + 1 #we can use hash table.get to handle error checking if not in hash table during reference

#         for num in nums2:
#             if num in counts and counts[num] > 0: #count has to be above 0 to make sure count is min of occurrences in each list
#                 res.append(num)
#                 counts[num] -= 1

#         return res

# O(n) space and time solution
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        intersection = []
        
        p1, p2 = 0,0
        
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                intersection.append(nums1[p1])
                p1+=1
                p2+=1
                continue
            if nums1[p1] < nums2[p2]:
                p1+=1
                continue
            if nums1[p1] > nums2[p2]:
                p2+=1
                continue
        
        return intersection
                
