class Solution:
    def maxArea(self, heights: List[int]) -> int:        
        L, R = 0, len(heights) - 1
        sol_dict = {}
        sol_dict["max"] = 0
        while L < R:
            water_container = min(heights[L], heights[R])* (R-L)
            sol_dict["max"] = max(sol_dict["max"], water_container)
            if heights[L]<heights[R]:
                L+=1
            elif heights[L]>heights[R]:
                R-=1
            else:
                R-=1
        return sol_dict["max"]