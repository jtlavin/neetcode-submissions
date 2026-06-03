import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_except_self = []
        for i in range(len(nums)):
            list_except_self = nums[:i] + nums[i+1:]
            _sum = 1
            for num in list_except_self:
                _sum *= num
            prod_except_self.append(_sum)  
            # prod_except_self.append(math.prod(list_except_self))

        return prod_except_self