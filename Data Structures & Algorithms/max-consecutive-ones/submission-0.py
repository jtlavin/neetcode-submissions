class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons = 0
        counter = 0
        for n in nums:
            if n==1:
                counter +=1
                max_cons = max(max_cons, counter)
            else:
                counter = 0
        return max_cons
