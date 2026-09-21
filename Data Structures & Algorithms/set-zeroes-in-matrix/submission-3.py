class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # podemos recorrer una matrix 
        filas_cero = [False]*len(matrix)
        columnas_cero = [False]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # si encontramos un 0
                if matrix[i][j]==0:
                    filas_cero[i]=True
                    columnas_cero[j]=True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):           
                if filas_cero[i]==True or columnas_cero[j]==True:
                    matrix[i][j]=0
        
        return 

        