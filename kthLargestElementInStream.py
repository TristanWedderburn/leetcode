class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # init heap to array
        self.minHeap = nums
        # convert array to heap in-place, in linear time
        heapq.heapify(self.minHeap)
        # heap to size k to retain kth largest element
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # O(logn) time complexity
         
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # O(logn) time complexity
        
        # ensure k elements only in heap
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # O(logn) time complexity
        
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
