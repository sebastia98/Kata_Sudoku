def check_columnas(sudoku):
    assert isinstance (sudoku, list)
    numero_maximo = len(sudoku)
    fila = 1
    for columna in range (numero_maximo):
        for elemento_fila in range (1, numero_maximo):
            if elemento_fila[columna][0] != elemento_fila[columna][fila]:
                return False
            fila += 1

if __name__ == "__main__":
    incorrect1 = [[1, 2, 3],
                  [2, 3, 1],
                  [2, 3, 1]]
    assert check_columnas(incorrect1) == False
