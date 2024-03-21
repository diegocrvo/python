"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""

open = close = 0
list = list()
while True:
    value = str(input('Digite a expressão: '))
    for simbol in value:
        if simbol == '(':
            open += 1
        if simbol == ')':
            close += 1
    if open == close:
        print(f'A expresão é válida.')
    else:
        print(f'A expresão não é válida.')
    open = close= 0
    comand = str(input('Deseja continuar?[S/N]: ')).strip()[0]
    if comand in 'Nn':
        break
print('\033[31mPrograma Encerrado.\033[m')