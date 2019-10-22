class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # for each interval, we either add it because it doesn't overlap or update last interval
        merged = []
        for interval in sorted(intervals):
            if not merged or merged[-1][-1]<interval[0]:
                merged.append(interval)
            else:
                merged[-1][-1] = max(merged[-1][-1], interval[-1])
        return merged
