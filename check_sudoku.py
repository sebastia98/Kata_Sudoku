from check_cuadrado import check_cuadrado
from check_numero import check_numero
from check_filas import check_filas

def check_sudoku(sudoku):
    return check_cuadrado(sudoku) and check_numero(sudoku) and check_filas(sudoku)