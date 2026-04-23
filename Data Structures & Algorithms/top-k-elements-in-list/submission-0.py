class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for n in nums:
            res[n] = res.get(n, 0) + 1

        res_sorted = [k for k,v in sorted(res.items(), 
                                          key=lambda item: item[1], 
                                          reverse=True)]
        return (res_sorted[:k])
        
        