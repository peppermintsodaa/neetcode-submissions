class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}

        for n in nums:
            frequent[n] = 1 + frequent.get(n, 0)

        heap = []
        for n in frequent:
            heapq.heappush(heap, (frequent[n], n))
            if len(heap) > k:
                heapq.heappop(heap)

        return [n for (v, n) in heap]