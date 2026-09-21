class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # podemos usar una lista auxiliar
        # en cada elemen
        res = []
        for i in range(len(intervals)):
            # estado 1: estrictamente despues
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            # estado 2: estricamente antes
            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            # estado 3: se solapan en alguno
            else:
                newInterval = [min(intervals[i][0], newInterval[0]),max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res

