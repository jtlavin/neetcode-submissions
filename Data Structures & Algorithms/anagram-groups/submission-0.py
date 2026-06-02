class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            sorted_word = sorted(word)
            sorted_word_join = "".join(sorted_word)
            if sorted_word_join in groups:
                groups[sorted_word_join].append(word)
            else:
                groups[sorted_word_join] = [word]
        return list(groups.values())