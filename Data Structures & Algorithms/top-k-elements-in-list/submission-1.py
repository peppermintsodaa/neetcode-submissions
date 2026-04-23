class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}

        for n in nums:
            frequent[n] = 1 + frequent.get(n, 0)

        sorted_frequent = dict(sorted(frequent.items(), key=lambda item: item[1], reverse = True))
        return list(sorted_frequent)[:k]