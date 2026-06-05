class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        # We need to check if the n-1 item is in the set

        longest = 0

        for num in set_nums:
            if num-1 not in set_nums:
                length=1
                while num + length in set_nums:
                    length +=1
                longest = max(longest, length)
        return longest


