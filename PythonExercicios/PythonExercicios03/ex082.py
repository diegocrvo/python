"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""

list = []
even = []
odd = []
while True:
    value = int(input('Enter a value: '))
    list.append(value)
    if value == 0:
        value = ''
    elif value % 2 == 0:
        even.append(value)
    else:
        odd.append(value)
    answer = str(input('Do you want to continue?[Y/N]: '))
    if answer in 'Nn':
        break
print('-' * 40)
print(f'The values entered were {list}')
print(f'The entered even values were {even}')
print(f'The entered odd values were {odd}')
