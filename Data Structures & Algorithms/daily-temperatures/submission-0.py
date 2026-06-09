class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results=[]
        for i in range(len(temperatures)-1):
            j = i+1
            days = 0
            found = False
            while j < len(temperatures):
                if temperatures[i]<temperatures[j]:
                    days+=1
                    results.append(days)
                    found = True
                    break
                else:
                    days+=1
                    j+=1
            if not found:
                results.append(0)

        results.append(0)
        return results