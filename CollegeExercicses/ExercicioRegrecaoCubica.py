from numpy import matrix, linalg
import numpy as np
import copy

#Inserindo as coordenadas dos pontos da tabela.
x0 = 0.5
y0 = 2500

x1 = 1
y1 = 2400

x2 = 2
y2 = 2000

x3 = 3
y3 = 1800

x4 = 4
y4 = 1500

m = 5

#Determinando as somas que compõem a matriz.
print("Para determinar a função y = a0 + a1 * x + a2 * x²")
soma1 = x0 + x1 + x2 + x3 + x4
soma2 = (x0**2) + (x1**2) + (x2**2) + (x3**2) + (x4**2)
soma3 = (x0**3) + (x1**3) + (x2**3) + (x3**3) + (x4**3)
soma4 = (x0**4) + (x1**4) + (x2**4) + (x3**4) + (x4**4)
soma5 = (x0**5) + (x1**5) + (x2**5) + (x3**5) + (x4**5)
soma6 = (x0**6) + (x1**6) + (x2**6) + (x3**6) + (x4**6)

soma7 = y0 + y1 + y2
soma8 = (x0 * y0) + (x1 * y1) + (x2 * y2)
soma9 = ((x0**2) * y0) + ((x1**2) * y1) + ((x2**2) * y2)
soma10 = ((x0**3) * y0) + ((x1**3) * y1) + ((x2**3) * y2)

#Apresentando o sistema matricial do método.
print("A * X = B")
matriz_A = np.array([[m, soma1, soma2, soma3], [soma1, soma2, soma3, soma4], [soma2, soma3, soma4, soma5], [soma3, soma4, soma5, soma6]], dtype=np.float64)
matriz_B = np.array([[soma7], [soma8], [soma9], [soma10]], dtype=np.float64)

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
for c in range(4):
    matriz_C = np.copy(matriz_A)
    for indiceL, linha in enumerate(matriz_C):
        linha[c] = matriz_B[indiceL, 0]
    matrizes.append(matriz_C)

matriz_A0, matriz_A1, matriz_A2, matriz_A3 = matrizes

det_A0 = linalg.det(matriz_A0)
det_A1 = linalg.det(matriz_A1)
det_A2 = linalg.det(matriz_A2)
det_A3 = linalg.det(matriz_A3)

# Determinando o valor das variáveis
a0 = det_A0 / det_A
a1 = det_A1 / det_A
a2 = det_A2 / det_A
a3 = det_A3 / det_A

print("\nResolvendo o sistema para determinar os coeficientes pela Regra de Cramer:\n")
print(f"det_A = {det_A}")
print(f"a0 = {a0}")
print(f"a1 = {a1}")
print(f"a2 = {a2}\n")
print(f"a3 = {a3}\n")

#Apresentando a função de segundo grau.
print("A função interpoladora é dada por:")
print("y = ", a0, "+", a1, "x", a2, "x²", "+", a3, "x³")

#Determinando y para x = 0.5
x = 0.5
y = a0 + (a1 * x) + (a2 * (x**2)) + (a3 * (x**3))
print("\nPara tal função, tem-se que:")
print("x = ", x, "Anos")
print("y = ", y, "Parafusos/dia")

#Cálculo do resíduo
y0i = a0 + (a1 * x0) + (a2 * (x0**2)) + (a3 * (x0**3))
y1i = a0 + (a1 * x1) + (a2 * (x1**2)) + (a3 * (x1**3))
y2i = a0 + (a1 * x2) + (a2 * (x2**2)) + (a3 * (x2**3))
y3i = a0 + (a1 * x3) + (a2 * (x3**2)) + (a3 * (x3**3))
y4i = a0 + (a1 * x4) + (a2 * (x4**2)) + (a3 * (x4**3))

R = ((y0 - y0i)**2) + ((y1 - y1i)**2) + ((y2 - y2i)**2) + ((y3 - y3i)**2) + ((y4 - y4i)**2)

print("\nResíduo = ", R)
