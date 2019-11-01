def check_columnas(sudoku):
    assert isinstance(sudoku, list)
    copiaSudoku = sudoku[:]
    numeroMaximo = len(sudoku)
    cantidadListas = numeroMaximo
    
    sudokuCompleto = []
    for fila in sudoku:
        for numero in fila:
            sudokuCompleto.append(numero)

    assert len(sudokuCompleto) == len(sudoku) ** 2

    columnaCopia = 0
    for columna in range(numeroMaximo):
        columnas = []
        columnas.append(sudokuCompleto[columna])
        columnaCopia = columna
        for _ in range(numeroMaximo - 1):
            columnaCopia += numeroMaximo
            columnas.append(sudokuCompleto[columnaCopia])
        if comprobarNumerosRepetidos(columnas):
            return False
    return True
    assert copiaSudoku == sudoku

def comprobarNumerosRepetidos(lista): #True si hay números repetidos, False si no hay números repetidos.
    elementosRepeticiones = {}
    for elemento in lista:
        if elemento in elementosRepeticiones:
            elementosRepeticiones[elemento] += 1
        else:
            elementosRepeticiones[elemento] = 1
    
    valores = list(elementosRepeticiones.values())
    for elemento in valores:
        if elemento > 1:
            return True
    return False


if __name__ == "__main__":

    assert comprobarNumerosRepetidos([2, 6, 7, 1, 3]) == False
    assert comprobarNumerosRepetidos([2, 4, 6, 8, 0, 7, 6, 4, 5]) == True
    assert comprobarNumerosRepetidos([2, 2]) == True
    assert comprobarNumerosRepetidos([2, 1, 3]) == False

    incorrect1 = [[1, 2, 3],
                  [2, 3, 1],
                  [2, 3, 1]]
    
    correct = [[1, 2, 3],
                [2, 3, 1],
                [3, 1, 2]]
    
    assert check_columnas(incorrect1) == False
    assert check_columnas(correct) == True