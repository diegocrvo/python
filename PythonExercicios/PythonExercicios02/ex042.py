"""Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
----------------------------------------------------------------------------------"""
print('-' * 50)
print('Analisador de Triângulo'.center(50))
print('-' * 50)
print('')

reta1 = float(input('Informe o primeiro segmento: '))
reta2 = float(input('Informe o segundo segmento: '))
reta3 = float(input('Informe o terceiro segmento: '))

if reta1 == reta2 == reta3:
    tipo = 'Equilátero'

elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
    tipo = 'Isósceles'

else:
    tipo = 'Escaleno'

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('É possível formar um triângulo!')

    if reta1 == reta2 == reta3:
        tipo = 'Equilátero'

    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        tipo = 'Isósceles'

    else:
        tipo = 'Escaleno'

    print(f'O triângulo formado é do tipo: {tipo}')

else:
    print('Não é possível formar um triângulo!')
