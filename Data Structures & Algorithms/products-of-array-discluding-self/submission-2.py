
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_except_self = []
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]


#        for i in range(len(nums)):
#            list_except_self = nums[:i] + nums[i+1:]
#            _sum = 1
#            for num in list_except_self:
#                _sum *= num
            # prod_except_self.append(_sum)  
            # prod_except_self.append(math.prod(list_except_self))

        return res