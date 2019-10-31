from check_sudoku import check_sudoku


def test_uno():
    correct = [[1, 2, 3],
                [2, 3, 1],
                [3, 1, 2]]
    assert check_sudoku(correct) == True
    
def test_dos():
    incorrect = [[1, 2, 3, 4],
                 [2, 3, 1, 3],
                 [3, 1, 2, 3],
                 [4, 4, 4, 2]]
    assert check_sudoku(incorrect) == False

def test_tres():
    incorrect1 = [[1, 2, 3],
                  [2, 3, 1],
                  [2, 3, 1]]
    assert check_sudoku(incorrect1) == False

def test_cuatro():
    incorrect2 = [[1, 2, 3, 4],
                  [2, 3, 1, 2],
                  [4, 1, 2, 3],
                  [2, 3, 1, 4]]
    assert check_sudoku(incorrect2) == False

def test_quinto():
    incorrect3 = [[1, 2, 3, 4, 5],
                  [2, 3, 1, 5, 6],
                  [4, 5, 2, 1, 3],
                  [3, 4, 5, 2, 1],
                  [5, 6, 4, 3, 2]]
    assert check_sudoku(incorrect3) == False

def test_seis(): 
    incorrect4 = [['a', 'b', 'c'],
                  ['b', 'c', 'a'],
                  ['c', 'a', 'b']]
    assert check_sudoku(incorrect4) == False

def test_siete():
    incorrect5 = [[1, 1.5],
                  [1.5, 1]]
    assert check_sudoku(incorrect5) == False

def test_siete():
    irregular = [[1, 2, 3],
                 [2, 3, 1]]
    assert check_sudoku(irregular) == False

def test_ocho():
    irregular2 = [[1, 2, 3],
                  [2, 3, 1],
                  [3, 1]]
    assert check_sudoku(irregular2) == False

def test_nueve():
    nuevo = [[]]
    assert check_sudoku(nuevo) == False