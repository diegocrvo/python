from numpy import matrix, linalg
import numpy as np
import copy

#Inserindo as coordenadas dos pontos da tabela.
x0 = 0
y0 = 0

x1 = 5
y1 = 2.846954

x2 = 10
y2 = 1.795416

m = 3

#Determinando as somas que compõem a matriz.
print("Para determinar a função y = a0 + a1 * x + a2 * x²")
soma1 = x0 + x1 + x2
soma2 = (x0 * x0) + (x1 * x1) + (x2 * x2)
soma3 = (x0 * x0 * x0) + (x1 * x1 * x1) + (x2 * x2 * x2)
soma4 = (x0 * x0 * x0 * x0) + (x1 * x1 * x1 * x1) + (x2 * x2 * x2 * x2)

soma5 = y0 + y1 + y2
soma6 = (x0 * y0) + (x1 * y1) + (x2 * y2)
soma7 = ((x0 * x0) * y0) + ((x1 * x1) * y1) + ((x2 * x2) * y2)

#Apresentando o sistema matricial do método.
print("A * X = B")
matriz_A = np.array([[m, soma1, soma2], [soma1, soma2, soma3], [soma2, soma3, soma4]], dtype=np.float64)
matriz_B = np.array([[soma5], [soma6], [soma7]], dtype=np.float64)

print('matriz_A')
print(matriz_A)
print('\nmatriz_B')
print(matriz_B)

# Determinante da matriz A
det_A = linalg.det(matriz_A)

# Determinando os coeficientes

if (det_A == 0):
    print('Esse sistema não pode ser resolvido pela Regra de Cramer!')
else:
    print("O determinante da matriz_A não é nulo.")

# Redefinindo as matrizes A1, A2 e A3
matrizes = []
for c in range(3):
    matriz_C = np.copy(matriz_A)
    for indiceL, linha in enumerate(matriz_C):
        linha[c] = matriz_B[indiceL, 0]
    matrizes.append(matriz_C)

matriz_A0, matriz_A1, matriz_A2 = matrizes

det_A0 = linalg.det(matriz_A0)
det_A1 = linalg.det(matriz_A1)
det_A2 = linalg.det(matriz_A2)

# Determinando o valor das variáveis
a0 = det_A0 / det_A
a1 = det_A1 / det_A
a2 = det_A2 / det_A

print("\nResolvendo o sistema para determinar os coeficientes pela Regra de Cramer:\n")
print(f"det_A = {det_A}")
print(f"a0 = {a0}")
print(f"a1 = {a1}")
print(f"a2 = {a2}\n")

#Apresentando a função de segundo grau.
print("A função interpoladora é dada por:")
print("y = ", a0, "+", a1, "x", a2, "x²")

#Determinando y para x = 1
x = 1
y = a0 + (a1 * x) + (a2 * x * x)
print("\nPara tal função, tem-se que:")
print("x = ", x, "ms")
print("y = ", y, "mm")

#Cálculo do resíduo
y0i = a0 + (a1 * x0) + (a2 * (x0 * x0))
y1i = a0 + (a1 * x1) + (a2 * (x1 * x1))
y2i = a0 + (a1 * x2) + (a2 * (x2 * x2))

R = ((y0 - y0i) * (y0 - y0i)) + ((y1 - y1i) * (y1 - y1i)) + ((y2 - y2i) * (y2 - y2i))

print("\nResíduo = ", R)