class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # resto = target - nums[i]
        # check if nums in resto

        kv ={}
        for i in range(len(nums)):
            if nums[i] in kv:
                return [kv[nums[i]], i]
            resto = target - nums[i]
            kv[resto] = i

        return False