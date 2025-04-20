import numpy
from math import cos, radians

#Definição dos parametros iniciais
k = 0.000000
tk = 0.000000
Pk = 600.000000
h = 0.500000

print("Parâmetros iniciais:")
print('t0 = ', tk)
print('P0 = ', Pk)
print('h = ', h)

#Criar loop
while (tk < 9.000000):

    #Definindo os termos k
    k1 = h * (10 * Pk * cos(tk))
    k2 = h * (10 * (Pk + (k1 / 2)) * cos(tk + (h / 2)))
    k3 = h * (10 * (Pk + ((3 / 4) * k2)) * cos(tk + ((3 / 4) * h)))
    k = k + 1

    print("/////////////////////////////////////////")
    print('k = ', k)
    print('k1 = ', k1)
    print('k2 = ', k2)
    print('k3 = ', k3)

    P = Pk + ((2 / 9) * k1) + ((1 / 3) * k2) + ((4 / 9) * k3)
    t = tk + h

    Pk = P
    tk = t

    print('tk = ', tk)
    print('Pk = ', Pk)

else:
    print("Fim!")
