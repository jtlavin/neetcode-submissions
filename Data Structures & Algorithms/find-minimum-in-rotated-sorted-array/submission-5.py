class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        # Elements are unique
        # Element is minimum if left side element is bigger
        # No importa para donde me mueva si checkeo i-1 y i+1?
        L, R = 0, len(nums) - 1

        while L < R:
            mid = (L+R)//2
            print(L, R, mid)
            if mid==0:
                if nums[mid]<nums[-1]:
                    return nums[mid]
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            elif nums[mid]> nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid

        