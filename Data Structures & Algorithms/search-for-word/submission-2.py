class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Solucion fuerza bruta seria
        # buscar la primera letra de la palabra en todas las rows
        # Cuando la encontremos en [i,j], empezar a buscar la 2da letra 
        # en la posicion [i-1,j], [i+1,j], [i,j+1], [i,j-1]
        # Si encontramos la letra 2 buscamos la 3 con el mismo algoritmo sin pasar de nuevo por [i_1,j_1] ni i_2,j_2

        # Que pasa si el primer find de word[0] no contiene el path correcto pero un 2do find si?

        # Si encontramos word[0]-> DFS

        def dfs(r,c, indice):
            if indice==len(word):
                return True

            if r<0 or r>=len(board):
                return False
            elif c<0 or c>=len(board[0]):
                return False
            elif board[r][c] != word[indice]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'

            found = (
                dfs(r+1,c, indice+1) or
                dfs(r-1,c, indice+1) or
                dfs(r,c+1, indice+1) or
                dfs(r,c-1, indice+1)
            )
            board[r][c] = temp
            return found
        
        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r,c, 0):
                        return True
        
        return False


        
