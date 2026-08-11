class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointer solution
        s_clean = [c for c in s if c.isalnum()]
        s_clean = [c.lower() for c in s_clean]

        l, r = 0, len(s_clean)-1
        while l<r:
            if s_clean[l]!=s_clean[r]:
                return False
            l+=1
            r-=1
        return True
