class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Aim to O(m*n), meaning for each word search it completly
        # If we sort then O(n*logn * m) probably
        res = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] +=1
            res[tuple(count)].append(s)

        return list(res.values())