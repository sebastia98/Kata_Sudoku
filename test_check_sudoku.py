from check_cuadrado import chech_cuadrado

def test_uno():
    correct = [[1, 2, 3],
               [2, 3, 1],
               [3, 1, 2]]
    assert check_cuadrado(correct) == True


def test_dos():
    incorrect = [[1, 2, 3, 4],
                 [2, 3, 1, 3],
                 [3, 1, 2, 3],
                 [4, 4, 4, 2]]
    assert check_cuadrado(incorrect) == False

def test_tres():
    incorrect1 = [[1, 2, 3],
                  [2, 3, 1],
                  [2, 3, 1]]
    assert check_cuadrado(incorrect1) == False

def test_cuatro():
    incorrect2 = [[1, 2, 3, 4],
                  [2, 3, 1, 2],
                  [4, 1, 2, 3],
                  [2, 3, 1, 4]]
    assert chech_cuadrado(incorrect2) == False

def test_quinto():
    incorrect3 = [[1, 2, 3, 4, 5],
                  [2, 3, 1, 5, 6],
                  [4, 5, 2, 1, 3],
                  [3, 4, 5, 2, 1],
                  [5, 6, 4, 3, 2]]
    assert chech_cuadrado(incorrect3) == False

def test_seis(): 
    incorrect4 = [['a', 'b', 'c'],
                  ['b', 'c', 'a'],
                  ['c', 'a', 'b']]
    assert chech_cuadrado(incorrect4) == False

def test_siete():
    incorrect5 = [[1, 1.5],
                  [1.5, 1]]
    assert chech_cuadrado(incorrect5) == False

def test_siete():
    irregular = [[1, 2, 3],
                 [2, 3, 1]]
    assert chech_cuadrado(irregular) == False

def test_ocho():
    irregular2 = [[1, 2, 3],
                  [2, 3, 1],
                  [3, 1]]
    assert chech_cuadrado(irregular2) == False

def test_nueve():
    nuevo = [[]]
    assert chech_cuadrado(nuevo) == False