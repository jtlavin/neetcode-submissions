import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_except_self = []
        for i in range(len(nums)):
            list_except_self = nums[:i] + nums[i+1:]
            prod_except_self.append(math.prod(list_except_self))

        return prod_except_self