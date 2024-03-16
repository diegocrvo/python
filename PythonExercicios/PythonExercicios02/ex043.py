"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule sei IMC e mostre seu status, conforme a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
--------------------------------------------------------------------------------"""
print('-' * 20)
print('Calculadora de IMC'.center(20))
print('-' * 20)
print('')

peso = float(input('Informe seu peso em Kg: '))
altura = float(input('Informe sua altura em m: '))
imc = peso / (altura ** 2)

print(f'\033[32mSeu IMC é {imc:.1f}')

if imc < 18.5:
    print('\033[31mVocê está abaixo do peso.')

elif 18.5 <= imc < 25:
    print('Você está com o peso ideal.')

elif 25 <= imc < 30:
    print('\033[33mVocê está com sobrepeso.')

elif 30 <= imc <= 40:
    print('\033[31mVocê está com obesidade.')

else:
    print('\033[35mVocê está com obesidade mórbida.')
