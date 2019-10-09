class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

#       bigger or smaller list doesn' t matter because we are looking for the min of occurrences in both lists
        counts = {}
        res = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1 #we can use hash table.get to handle error checking if not in hash table during reference

        for num in nums2:
            if num in counts and counts[num] > 0: #count has to be above 0 to make sure count is min of occurrences in each list
                res.append(num)
                counts[num] -= 1

        return res
