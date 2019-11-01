def check_columnas(sudoku):
    
    assert isinstance (sudoku, list)
    copia_sudoku = sudoku[:]
    numero_maximo = len(sudoku)
    columna = 0
    for fila in range (1, numero_maximo):
        if sudoku[columna][0] != sudoku[columna][fila]:
            return False
        columna += 1
    return True
    assert copia_sudoku == sudoku    
 

if __name__ == "__main__":
    incorrect1 = [[1, 2, 3],
                  [2, 3, 1],
                  [2, 3, 1]]
    assert check_columnas(incorrect1) == False
    correct = [[1, 2, 3],
                [2, 3, 1],
                [3, 1, 2]]
    assert check_columnas(correct) == True
