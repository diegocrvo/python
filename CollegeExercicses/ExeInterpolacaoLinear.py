from numpy import matrix, linalg
import numpy as np
import copy

#Inserindo as coordenadas dos pontos da tabela.
x0 = 6000
y0 = 1.375

x1 = 6500
y1 = 1.428

x2 = 7000
y2 = 1.482

x3 = 7500
y3 = 1.534

x4 = 8000
y4 = 1.585

m = 5

#Apresentando o sistema matricial do método.
print("A * X = B")
matriz_A = np.array([[1, x0, x0**2, x0**3, x0**4], [1, x1, x1**2, x1**3, x1**4], [1, x2, x2**2, x2**3, x2**4], [1, x3, x3**2, x3**3, x3**4], [1, x4, x4**2, x4**3, x4**4]], dtype=np.float64)
matriz_B = np.array([[y0], [y1], [y2], [y3], [y4]], dtype=np.float64)

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
for c in range(5):
    matriz_C = np.copy(matriz_A)
    for indiceL, linha in enumerate(matriz_C):
        linha[c] = matriz_B[indiceL, 0]
    matrizes.append(matriz_C)

matriz_A0, matriz_A1, matriz_A2, matriz_A3, matriz_A4 = matrizes

det_A0 = linalg.det(matriz_A0)
det_A1 = linalg.det(matriz_A1)
det_A2 = linalg.det(matriz_A2)
det_A3 = linalg.det(matriz_A3)
det_A4 = linalg.det(matriz_A4)

# Determinando o valor das variáveis
a0 = det_A0 / det_A
a1 = det_A1 / det_A
a2 = det_A2 / det_A
a3 = det_A3 / det_A
a4 = det_A4 / det_A

print("\nResolvendo o sistema para determinar os coeficientes pela Regra de Cramer:\n")
print(f"det_A = {det_A}")
print(f"a0 = {a0}")
print(f"a1 = {a1}")
print(f"a2 = {a2}")
print(f"a2 = {a3}")
print(f"a2 = {a4}\n")

#Apresentando a função de segundo grau.
print("A função interpoladora é dada por:")
print("y = ", a0, "+", a1, "x", a2, "x²")

#Determinando y para x = 0,7
x = 6850
y = a0 + (a1 * x) + (a2 * (x**2)) + (a3 * (x**3)) + (a4 * (x**4))
print("\nPara tal função, tem-se que:")
print("x = ", x, "Anos")
print("y = ", y, "Parafusos/dia")

#Cálculo do resíduo
y0i = a0 + (a1 * x0) + (a2 * (x0**2))
y1i = a0 + (a1 * x1) + (a2 * (x1**2))
y2i = a0 + (a1 * x2) + (a2 * (x2**2))
y3i = a0 + (a1 * x3) + (a2 * (x3**2)) 
y4i = a0 + (a1 * x4) + (a2 * (x4**2)) 

R = ((y0 - y0i)**2) + ((y1 - y1i)**2) + ((y2 - y2i)**2) + ((y3 - y3i)**2) + ((y4 - y4i)**2)

print("\nResíduo = ", R)
