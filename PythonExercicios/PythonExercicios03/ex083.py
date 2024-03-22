"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""

exp = str(input('Digite a expresão: '))
list = []
for simb in exp:
    if simb == '(':
        list.append('(')
    elif simb == ')':
        if len(list) > 0:
            list.pop()
        else:
            list.append(')')
            break
if len(list) == 0:
    print(f'A expresão é válida.')
else:
    print(f'A expresão é inválida.')
print('\033[31mPrograma Encerrado.\033[m')
