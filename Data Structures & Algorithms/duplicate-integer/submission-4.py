class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        num_set = list(set(nums))
        num_set.sort()

        return nums != num_set