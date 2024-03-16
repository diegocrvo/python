# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
# ---------------------------------------------------------------------------
print('-' * 50)
print('Analisador de Triângulo'.center(50))
print('-' * 50)
print('')
reta1 = float(input('Informe o primeiro segmento: '))
reta2 = float(input('Informe o segundo segmento: '))
reta3 = float(input('Informe o terceiro segmento: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')
