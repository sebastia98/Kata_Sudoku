def check_numero(sudoku):
    assert isinstance(sudoku, list)
    copia_sudoku = sudoku[:]
    for fila in sudoku:
        for elemento in fila:
            if isinstance(elemento, int) == False:
                return False
    assert copia_sudoku == sudoku
    return True
if __name__ == "__main__":
    incorrect = [[1, 2, 'p'], 
                [2, 3, 2],
                [3, 1, 's']]
    correct = [[1, 2, 3],
                [2, 3, 1],
                [3, 1, 2]]
    assert check_numero(incorrect) == False
    assert check_numero(correct) == True
    incorrect4 = [['a', 'b', 'c'],
                  ['b', 'c', 'a'],
                  ['c', 'a', 'b']]
    assert check_numero(incorrect4) == False


