class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Quiero tomar cada elemento de text1 y revisar uno por uno si esta en text2
        # Pero el orden es importante, si el elemento text1[0] está en text2[1]
        # tengo que revisar si text1[1] está en text2[2:] no la lista completa
        # necesito alguna forma de actualizar cuando encuentro un match

        if text1==text2: # Caso son iguales
            return len(text1)
        if len(set(text1)&set(text2)) == 0: # Caso no coinciden en nada
            return 0

        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        
        # Recorrer en reversa
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        print(dp)
        return dp[0][0]