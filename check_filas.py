def check_filas(sudoku):
    assert isinstance (sudoku, list)
    copia_sudoku = sudoku[:]
    for fila in sudoku:
        for elemento in fila:
            if elemento > len(fila) or contar_elementos(elemento, fila) > 1:
                return False  
    return True
    assert copia_sudoku == sudoku

def contar_elementos(entero, lista):
    repeticiones = 0
    for elemento in lista:
        if entero == elemento:
            repeticiones += 1
    return repeticiones

if __name__ == "__main__":
    incorrect = [[1, 2, 3, 4],
                 [2, 3, 1, 3],
                 [3, 1, 2, 3],
                 [4, 4, 4, 2]]
    assert check_filas(incorrect) == False
    correct = [[1, 2, 3],
                [2, 3, 1],
                [3, 1, 2]]
    assert check_filas(correct) == True

