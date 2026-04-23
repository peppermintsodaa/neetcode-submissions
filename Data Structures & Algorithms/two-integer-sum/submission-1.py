class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        
        for i, n in enumerate(nums):
            count[n] = i

        for i, n in enumerate(nums):
            difference = target - n

            if difference in count and count[difference] != i:
                return [i, count[difference]]

        return []
        

        