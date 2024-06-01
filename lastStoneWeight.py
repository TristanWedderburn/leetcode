class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap
        # init max heap with stones
        # pop two heaviest and then push the residual stone
        # check until <= 1 stones left

        # we can use the heapq implementation that defaults to a minheap as a maxheap by multiplying all of the stone weights by -1
        maxHeap = [-1*stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            print("heap", maxHeap)

            # take two heaviest stones
            y = -1*heapq.heappop(maxHeap)
            x = -1*heapq.heappop(maxHeap)

            residualStone = y - x
            
            if (residualStone > 0):
                heapq.heappush(maxHeap, -1*residualStone)

        if len(maxHeap) > 0:
            return -1*maxHeap[-1]
        else:
            return 0
