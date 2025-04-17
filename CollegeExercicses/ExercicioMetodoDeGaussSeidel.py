# Método de Gauss-Seidel

from numpy import matrix
import numpy as np

# Definindo as equações a serem utilizadas nas iteralções
print("""Equações para as iterações
      t = (13 - x - (2 * n)) / 15 
      x = (10 - t - n) / 8
      n = (-4 - t - x) / 3""")

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
while (erro_t >= 0.01 and erro_x >= 0.01 and erro_n >= 0.01):
    
    # Determinando os novos valores das variáveis
    k1 = k + 1 # incremento no parâmetro de iteração
    x1 = (10 - t - (2 * n)) / 8
    t1 = (13 - x1 - (2 * n)) / 15
    n1 = (-4 - t1 - x1) / 3

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
