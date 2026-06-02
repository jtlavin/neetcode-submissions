class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i, value in enumerate(nums):
            dict_nums[value] = i

        for i, value in enumerate(nums):
            diff = target - value
            if diff in dict_nums and dict_nums[diff]!= i:
                return sorted([i, dict_nums[diff]])
        