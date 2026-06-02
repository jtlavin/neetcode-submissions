class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for value in nums:
            if d.get(value, None):
                return True
            else:
                d[value] = 1
        return False

