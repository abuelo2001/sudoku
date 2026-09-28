# ============================================================
# EXAMEN - RESOLVEDOR DE SUDOKU EN PYTHON
# Alumno: Joan Sebastian Garcia Orozco
# ============================================================

# Sudoku proporcionado en el examen.
# Los espacios vacíos se representan con 0.

sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


# ------------------------------------------------------------
# Función para mostrar el Sudoku
# ------------------------------------------------------------
def mostrar_sudoku(tablero):
    print("\n+-------+-------+-------+")

    for fila in range(9):

        print("|", end=" ")

        for columna in range(9):

            # Si hay un 0, mostramos un punto
            if tablero[fila][columna] == 0:
                print(".", end=" ")
            else:
                print(tablero[fila][columna], end=" ")

            # Separación de los bloques 3x3
            if (columna + 1) % 3 == 0:
                print("|", end=" ")

        print()

        # Línea horizontal cada 3 filas
        if (fila + 1) % 3 == 0:
            print("+-------+-------+-------+")


# ------------------------------------------------------------
# Buscar una casilla vacía
# ------------------------------------------------------------
def buscar_vacio(tablero):

    for fila in range(9):
        for columna in range(9):

            if tablero[fila][columna] == 0:
                return fila, columna

    # Si no existen ceros, el Sudoku está completo
    return None


# ------------------------------------------------------------
# Comprobar si un número puede colocarse
# ------------------------------------------------------------
def numero_valido(tablero, numero, fila, columna):

    # Revisar que el número no exista en la fila
    for i in range(9):
        if tablero[fila][i] == numero:
            return False

    # Revisar que el número no exista en la columna
    for i in range(9):
        if tablero[i][columna] == numero:
            return False

    # Encontrar el inicio del bloque 3x3
    inicio_fila = (fila // 3) * 3
    inicio_columna = (columna // 3) * 3

    # Revisar el bloque 3x3
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):

            if tablero[i][j] == numero:
                return False

    return True


# ------------------------------------------------------------
# Resolver Sudoku utilizando Backtracking
# ------------------------------------------------------------
def resolver_sudoku(tablero):

    vacio = buscar_vacio(tablero)

    # Si ya no existen espacios vacíos, terminamos
    if vacio is None:
        return True

    fila, columna = vacio

    # Probar números del 1 al 9
    for numero in range(1, 10):

        if numero_valido(tablero, numero, fila, columna):

            tablero[fila][columna] = numero

            # Intentamos continuar resolviendo
            if resolver_sudoku(tablero):
                return True

            # Si no funciona, regresamos la casilla a 0
            tablero[fila][columna] = 0

    return False


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("=" * 45)
print("       RESOLVEDOR DE SUDOKU")
print("       Joan Sebastian Garcia Orozco")
print("=" * 45)

print("\nINSTRUCCIONES:")
print("Este programa resolverá automáticamente")
print("el Sudoku proporcionado en el examen.")
print("Los puntos representan espacios vacíos.")

print("\nSUDOKU ORIGINAL:")
mostrar_sudoku(sudoku)

input("\nPresiona ENTER para resolver el Sudoku...")

if resolver_sudoku(sudoku):

    print("\nSUDOKU RESUELTO:")
    mostrar_sudoku(sudoku)

else:
    print("\nEl Sudoku no tiene solución.")

input("\nPresiona ENTER para finalizar...")