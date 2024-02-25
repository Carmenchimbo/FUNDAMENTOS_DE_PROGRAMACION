# Definir la matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Definir el valor a buscar
valor_a_buscar = 8

# Variable para indicar si se encontró el valor
encontrado = False

# Buscar el valor en la matriz
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] == valor_a_buscar:
            print(f"El valor {valor_a_buscar} se encontró en la posición ({i}, {j}).")
            encontrado = True
            break

# Mostrar mensaje si el valor no se encontró
if not encontrado:
    print(f"El valor {valor_a_buscar} no se encuentra en la matriz.")
