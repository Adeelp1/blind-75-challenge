class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}
        for i,num in enumerate(nums):
            difference = target - num
            if difference in num_indices:
                return [num_indices[difference], i]
            num_indices[num]=i