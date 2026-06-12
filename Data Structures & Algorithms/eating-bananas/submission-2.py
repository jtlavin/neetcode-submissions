class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        
        # K nunca va a ser mayor que max(piles)
        # sino me sobraria tiempo y podria reducir K

        # horas totales para un K es horas por pile
        # redondeado hacia arriba

        # Min k va de 1 a max(piles)

        L, R = 1, max(piles)
        possible_k = []
        while L <= R:
            total_hours = 0
            k = (L+R)//2
            for pile in piles:
                total_hours += math.ceil(pile/k)
            if total_hours<=h:
                res = k
                R = k -1
            else:
                L = k + 1
        
        return res


        