class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Contar apariciones -> hash map
        # ordenar un diccionario -> sorted(dict.items(), key = lambda x: x[1], ascending = False)
        # Top K in list = list[:k] if sorted

        counter = {}
        for num in nums:
            counter[num] = 1+ counter.get(num, 0)

        counter = sorted(counter.items(), key = lambda x:x[1], reverse=True)
        res = [i[0] for i in counter]
        print(res[:k])
        return res[:k]