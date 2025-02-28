# Método de Gauss-Jordan
from numpy import matrix, linalg
import numpy as np

# Criando as matrizes
print("A * X = B é preciso escrever como I * X = S")
matriz_A = np.array([[2.0, 1.0, 1.0], [0.3, 2.0, 0.25], [1.0, 1.0, 2.0]])
matriz_B = np.array([[39.0], [13.0], [45.0]])

print('matriz_A:')
print(f'{matriz_A}\n')
print('matriz_B:')
print(f'{matriz_B}\n')

# Criando a matriz inversa da Matriz A

print("Sabendo que A * A_inv = I, a solução pode ser dada por S = A_inv * B\n")

matriz_A_inv = linalg.inv(matriz_A)

print('Matriz_A_inv:')
print(f'{matriz_A_inv}\n')

# Solução

matriz_S = np.matmul(matriz_A_inv, matriz_B)

print('Solução Matriz_S:')
print(matriz_S)
