class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i, value in enumerate(nums):
            diff = target - value
            if diff in dict_nums:
                return [dict_nums[diff], i]
            dict_nums[value] = i