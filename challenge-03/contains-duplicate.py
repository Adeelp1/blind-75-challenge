class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        array = set()
        for i in nums:
            if i in array:
                return True
            else:
                array.add(i)
        return False