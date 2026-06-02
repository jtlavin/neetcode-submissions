class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        sorted_items = sorted(num_count.items(), key = lambda x: x[1], reverse=True)

        return [item[0] for item in sorted_items[:k]]