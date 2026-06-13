class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
            
        for i in range(len(nums)):
            if i == 0:
                if nums[i]<nums[-1]:
                    return nums[i]
            
            if nums[i]< nums[i-1]:
                return nums[i]