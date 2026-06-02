class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, value in enumerate(nums):
            for j, val in enumerate(nums[1:]):
                if value + val == target:
                    if i!=j+1:
                        return sorted([i,j+1])
        