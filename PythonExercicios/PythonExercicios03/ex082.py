"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""

list = []
listpar = []
listimpar = []
while True:
    value = int(input('Digite um número: '))
    list.append(value)
    comand = str(input('Deseja continuar?[S/N]: '))
    if value == 0:
        value = ''
    elif value % 2 == 0:
        listpar.append(value)
    else:
        listimpar.append(value)
    if comand in 'Nn':
        break
print(f'Os valores digitados foram {list}')
print(f'Os valores pares digitados foram {listpar}')
print(f'Os valores ìmpares digitados foram {listimpar}')
