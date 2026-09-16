class Solution:
    def climbStairs(self, n: int) -> int:
        # parece como buscar combinatorias en que 1 y 2 puedan sumar n
        memo = {}

        def helper(i: int) -> int:
            if i <= 2:
                return i
            
            if i in memo:
                return memo[i]
            
            memo[i] = helper(i-1) + helper(i-2)
            return memo[i]

        return helper(n)
        

        