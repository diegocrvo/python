# Método de Gauss-Seidel

from numpy import matrix
import numpy as np

# Definindo as equações a serem utilizadas nas iteralções
print("""Equações para as iterações
      t = (39 - x - n) / 2
      x = (13 - (0.3 * t) - (0.25 * n)) / 2
      n = (45 - t - x) / 2""")

# Identificando as variáveis e o Parâmetro inicial
t = 0.0
x = 0.0
n = 0.0
k = 0
matriz_X0 = np.array([[t], [x], [n]])
print('Parâmetro inicial: Matriz_X0')
print(matriz_X0)

erro_t = 1
erro_x = 1
erro_n = 1
while (erro_t >= 0.0000000001 and erro_x >= 0.0000000001 and erro_n >= 0.0000000001):
    
    # Determinando os novos valores das variáveis
    k1 = k + 1 # incremento no parâmetro de iteração
    t1 = (39 - x - n) / 2
    x1 = (13 - (0.3 * t1) - (0.25 * n)) / 2
    n1 = (45 - t1 - x1) / 2

    erro_t = abs(t1 - t)
    erro_x = abs(x1 - x)
    erro_n = abs(n1 - n)

    # Atualização dos valores das variáveis
    k = k1
    t = t1
    x = x1
    n = n1

    #Valores de cada iteração
    print(f'k = {k}')
    print(f't = {t}')
    print(f'x = {x}')
    print(f'n = {n}')
    print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
else:
    print('A última iteração nos diz que')
    matriz_S = np.array([[t], [x], [n]])
    print('Solução: Matriz_S')
    print(matriz_S)
