class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <=1:
            return intervals
    
        intervals.sort() #sort based on interval start index
        result = []
        merged = intervals[0]
        
        for i in range(len(intervals)):
            if i+1 < len(intervals) and intervals[i+1][0]<=merged[1]:
                if intervals[i+1][1]>merged[1]:
                    merged[1] = intervals[i+1][1]
            else:
                result.append(merged)
                if i+1 < len(intervals):
                    merged = intervals[i+1]
            
        return result
