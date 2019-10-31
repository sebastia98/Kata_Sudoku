def check_cuadrado (sudoku):
    assert isinstance (sudoku, list)
    copia_sudoku = sudoku[:]
    filas=len(sudoku)
    for columna in sudoku:
        if len(columna) != filas:
            return False
    assert sudoku == copia_sudoku
    return True

if __name__ == "__main__":
    correct = [[1, 2, 3],
                [2, 3, 1],
                [3, 1, 2]]
    
    irregular = [[1, 2, 3],
                 [2, 3, 1]]
    
    assert check_cuadrado(irregular) == False
    assert check_cuadrado(correct) == True
