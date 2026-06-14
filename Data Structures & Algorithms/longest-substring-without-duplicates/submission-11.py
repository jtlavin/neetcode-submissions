class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        guardia = set()
        length = 0

        if len(s)==1:
            return 1

        for R in range(len(s)):
            while s[R] in guardia:
                guardia.remove(s[L])
                L += 1
            guardia.add(s[R])
            length = max(length, R - L + 1)

        return length