"""Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de
zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
-------------------------------------------------------------------------------------------------"""
count = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
         'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
         'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
         'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
         'Dezenove', 'Vinte')

while True:
    print('-' * 40)
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'O número digitado foi {count[num]}.')
        comando = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if comando == 'N':
            break
        else:
            num = ''
print('\033[31mPrograma Encerrado.\033[m')
