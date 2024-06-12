from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter in python to count frequencies

        # create frequency map
        c = Counter(nums)

        # sorted_items = sorted(c.items(), key=lambda item: item[1], reverse=True)
        # sorted_keys = [item[0] for item in sorted_items]
        # return sorted_keys[:k]

        # use min heap
        freqs = []
        for num, freq in c.items():
            heapq.heappush(freqs, (freq, num)) # heap is sorted by first index

            if len(freqs) > k: # only maintain k elements in heap
                heapq.heappop(freqs) # pop min frequency
        
        return [p[1] for p in reversed(freqs)] # return only the nums
                
