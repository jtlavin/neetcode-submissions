class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # First we are going to look using binary search
        # if the target may exist inside a row
        L, R = 0, len(matrix)-1

        while L<=R:
            mid = (L+R)//2
            print(L, R)
            if target > matrix[mid][-1]:
                L = mid +1
            elif target < matrix[mid][0]:
                R = mid - 1
            else:
                break
            
        if L>R:
            return False
        else:
            L_col, R_col = 0, len(matrix[mid]) - 1

            while L_col <= R_col:
                mid_col = (L_col+R_col)//2
                print(L_col, R_col)
                if target > matrix[mid][mid_col]:
                    L_col = mid_col + 1
                elif target < matrix[mid][mid_col]:
                    R_col = mid_col - 1
                else:
                    return True
            return False

                
        
        
        
