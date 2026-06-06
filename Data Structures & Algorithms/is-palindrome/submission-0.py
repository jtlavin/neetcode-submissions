class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointer solution
        s_clean = ''.join(c for c in s if c.isalnum())
        s_clean = s_clean.lower()

        L, R = 0, len(s_clean)-1
        while L < R:
            if s_clean[L] != s_clean[R]:
                return False
            L += 1
            R -= 1
            
        return True
