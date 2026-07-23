class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_dict = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in complement_dict:
                return [complement_dict[nums[i]], i]
            complement_dict[complement] = i
        
            