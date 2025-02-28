# Regra de Cramer

from numpy import matrix, linalg
import numpy as np
import copy

# Criando as matrizes
print("A * X = B\n")
matriz_A = np.array([[2.0, 1.0, 1.0], [0.3, 2.0, 0.25], [1.0, 1.0, 2.0]])
matriz_B = np.array([[39.0], [13.0], [45.0]])

print('matriz_A:')
print(f'{matriz_A}\n')
print('matriz_B:')
print(f'{matriz_B}\n')

# Determinante da matriz A
det_A = linalg.det(matriz_A)

# Determinando os coeficientes

if (det_A == 0):
    print('Esse sistema não pode ser resolvido pela Regra de Cramer!')
else:
    print("O determinante da matriz_A não é nulo.")
    print(f"det_A = {det_A}\n")

# Redefinindo as matrizes A1, A2 e A3
matrizes = []
for c in range(3):
    matriz_C = copy.deepcopy(matriz_A)
    for indiceL, linha in enumerate(matriz_C):
        linha[c] = matriz_B[indiceL, 0]
    matrizes.append(matriz_C)

matriz_A1, matriz_A2, matriz_A3 = matrizes
print("Substituindo a coluna i da matriz Ai pelos elementos da matriz B, tem-se:")
print('matriz_A1')
print(matriz_A1)
det_A1 = linalg.det(matriz_A1)
print(f'det_A1 = {det_A1}\n')

print('matriz_A2')
print(matriz_A2)
det_A2 = linalg.det(matriz_A2)
print(f'det_A2 = {det_A2}\n')

print('matriz_A3')
print(matriz_A3)
det_A3 = linalg.det(matriz_A3)
print(f'det_A3 = {det_A3}\n')

# Determinando o valor das variáveis
t = det_A1 / det_A
x = det_A2 / det_A
n = det_A3 / det_A

print(f"t = {t}")
print(f"x = {x}")
print(f"n = {n}\n")

# Solução
matriz_S = np.array([[t], [x], [n]])
print('Solução: Matriz_S')
print(matriz_S)
